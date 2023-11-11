from django import template
from django.urls import reverse

from easy_cms.models import Page

register = template.Library()


@register.inclusion_tag("easy_cms/nav.html", takes_context=True)
def nav(context, content="content"):
    request = context["request"]

    menu_items = []
    for page in Page.objects.filter(parent__isnull=True):
        menu_item = {
            "label": page.title,
            "url": "/" + page.slug,
            "menu_items": [],
            "sub_urls": [],
        }

        for child_page in page.children.all():
            menu_item["sub_urls"].append(child_page.slug)
            menu_item["menu_items"].append(
                {
                    "label": child_page.title,
                    "url": "/" + child_page.slug,
                }
            )

        menu_items.append(menu_item)

        # Second check whether there is a sub item active
        sub_active = False
        for sub_url in menu_item.get("sub_urls"):
            if request.path.startswith(sub_url):
                sub_active = True

        # active main items
        if request.path[1:].startswith(menu_item.get("url", "NO!")) or sub_active:
            menu_item["active"] = True
        else:
            menu_item["active"] = False

        # active sub items
        for sub_item in menu_item.get("menu_items", []):
            if request.path.startswith(sub_item["url"]):
                sub_item["active"] = True
            else:
                sub_item["active"] = False

    display_edit = request.path.find("edit") == -1
    return {
        "menu_items": menu_items,
        "margin_top": 30 if content == "content" else 60,
        "request": request,
        "display_edit": display_edit,
        "display_view": not display_edit,
        "page": context.get("page"),
    }
