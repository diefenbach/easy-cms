def render_cbv(view, request, method, url, kwargs):
    request.META["method"] = request.method = method
    response = view.as_view()(request, **kwargs)

    if url:
        response["HX-Push-Url"] = url

    return response
