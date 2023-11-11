from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from easy_cms import models
from easy_cms.utils import render_cbv
from .models import Component, Page, Title


class FaviconView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("")


class HomeView(TemplateView):
    template_name = "easy_cms/home.html"


class PageView(TemplateView):
    template_name = "easy_cms/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = Page.objects.get(slug=kwargs.get("slug"))
        context["page"] = page
        context["page_rendered"] = page.render(self.request)

        return context


class EditView(TemplateView):
    template_name = "easy_cms/edit.html"

    def get_component_form(self, component_id):
        component = Component.objects.get(pk=component_id)
        return component.get_edit_form()

    def get_first_component(self, **kwargs):
        slug = kwargs.get("slug")
        return Component.objects.filter(page__slug=slug).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if c_id := kwargs.get("component_id"):
            context["component_id"] = c_id

        page = Page.objects.get(slug=kwargs.get("slug"))
        context["page"] = page
        context["rendered_page"] = page.render(self.request, for_edit=True, **kwargs)

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # If we have a component_id, we're editing a component
        if component_id := kwargs.get("component_id"):
            context["form"] = self.get_component_form(component_id)
            return self.render_to_response(context)

        # If we have no component, we try to get first one and redirect to it
        elif component := self.get_first_component(**kwargs):
            context["form"] = self.get_component_form(component.id)
            kwargs["component_id"] = component.id
            url = reverse("ec:edit-component", kwargs=kwargs)
            return HttpResponseRedirect(url)

        # If there is no component, we don't display a component form
        else:
            return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        component_id = kwargs.get("component_id")
        page_slug = kwargs.get("slug")
        page = get_object_or_404(Page, slug=page_slug)

        if self.request.POST.get("cancel-page-structure"):
            context = self.get_context_data(**kwargs)
            context["form"] = self.get_component_form(component_id)
            return self.render_to_response(context)

        elif 1:
            component = Component.objects.get(pk=kwargs.get("component_id"))
            form = component.get_edit_form(data=request.POST)
            if form.is_valid():
                form.save()
            context = {"form": form, **self.get_context_data(**kwargs)}

        context = self.get_context_data(**kwargs)
        context["form"] = self.get_component_form(component.id)
        return self.render_to_response(context)


def save_components_structure(request, **kwargs):
    page = get_object_or_404(Page, slug=kwargs.get("slug"))

    for i, c_id in enumerate(request.POST.getlist("component")):
        if c_id in ["Title", "Paragraph", "ParagraphTwoCols", "Image"]:
            model_class = getattr(models, c_id)
            component = model_class.objects.create(page=page, order=i)
            component.set_content(content=f"New {c_id}")
        else:
            component = Component.objects.get(pk=c_id)
            component.order = i
        component.save()

    return render_cbv(EditView, request, "GET", url=None, kwargs=kwargs)


def delete_component(request, **kwargs):
    component = get_object_or_404(Component, pk=kwargs.get("component_id"))
    component.delete()

    page = get_object_or_404(Page, slug=kwargs.get("slug"))
    kwargs["component_id"] = page.components.first().id

    url = reverse("ec:edit-component", kwargs=kwargs)
    return render_cbv(EditView, request, "GET", url=url, kwargs=kwargs)
