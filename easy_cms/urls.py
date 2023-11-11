from django.urls import path

from easy_cms import views

app_name = "ec"

urlpatterns = [
    path(
        "",
        views.HomeView.as_view(),
        name="home",
    ),
    path(
        "favicon.ico",
        views.FaviconView.as_view(),
        name="home",
    ),
    path(
        "<slug>",
        views.PageView.as_view(),
        name="page",
    ),
    path(
        "<slug>/edit",
        views.EditView.as_view(),
        name="edit",
    ),
    path(
        "<slug>/edit/<component_id>",
        views.EditView.as_view(),
        name="edit-component",
    ),
    path(
        "<slug>/save-components-structure",
        views.save_components_structure,
        name="save-components-structure",
    ),
    path(
        "<slug>/edit/<component_id>/delete",
        views.delete_component,
        name="delete-component",
    ),
]
