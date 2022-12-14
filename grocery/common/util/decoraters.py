def api_allow_all(view_func):
    def wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            request.is_authenticated = False
        else:
              request.is_authenticated = True
        return view_func(request, *args, **kwargs)
    return wrapped_view_func