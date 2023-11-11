from django import forms
from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from polymorphic.models import PolymorphicModel


class Page(models.Model):
    template = "easy_cms/components/page.html"

    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=50)
    order = models.IntegerField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def render(self, request=None, for_edit=False, **kwargs):
        rendered_components = []
        for component in self.components.all():
            rendered_components.append(
                component.render(request=request, for_edit=for_edit, **kwargs)
            )

        context = {"components": rendered_components}
        return render_to_string(self.template, context, request)


class Component(PolymorphicModel):
    order = models.IntegerField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="components")
    css_class = models.CharField(max_length=50, blank=True, default="")

    class Meta:
        ordering = ["order"]

    def get_edit_form(self, exclude=None, data=None):
        exclude = exclude or []
        if "order" in "exclude":
            exclude.remove("order")

        class ComponentForm(forms.ModelForm):
            class Meta:
                model = self.__class__
                exclude = ["order", "page"]

        return ComponentForm(instance=self, data=data)

    def set_content(self, content):
        self.content = content

    def type(self):
        return self.__class__.__name__

    def render(self, request=None, for_edit=False, **kwargs):
        if component_id := kwargs.get("component_id"):
            active = self.id == int(component_id)
        else:
            active = False

        context = {
            "object": self,
            "active": active,
            "for_edit": for_edit,
        }
        return render_to_string(self.template, context, request)


class Title(Component):
    template = "easy_cms/components/title.html"

    tag = models.CharField(max_length=20, default="h1")
    content = models.CharField(max_length=100)


class Paragraph(Component):
    template = "easy_cms/components/paragraph.html"

    content = models.TextField()


class ParagraphTwoCols(Component):
    template = "easy_cms/components/paragraph_two_cols.html"

    col_1 = models.TextField()
    col_2 = models.TextField()

    def set_content(self, content):
        self.col_1 = content
        self.col_2 = content


class Image(Component):
    template = "easy_cms/components/image.html"

    alt = models.CharField(max_length=100, blank=True, default="")
    image_title = models.CharField(max_length=100, blank=True, default="")
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    image_file = models.ImageField(upload_to="images", blank=True, null=True)

    def get_content(self, content):
        pass
