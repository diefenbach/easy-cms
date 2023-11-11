from django.contrib import admin

from easy_cms.models import Page, Paragraph, ParagraphTwoCols, Title, Image


admin.site.register(Page)
admin.site.register(Paragraph)
admin.site.register(Title)
admin.site.register(Image)
admin.site.register(ParagraphTwoCols)
