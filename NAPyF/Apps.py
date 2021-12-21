from NAPyF.App import App
from NAPyF.Types import Route, Method
from NAPyF.RequestFunctions import *


def default():
    app = App('default')
    default_get_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.GET.value,
        request_function=no_function
    )
    app.add_route(default_get_route)
    default_post_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.POST.value,
        request_function=default_post
    )
    app.add_route(default_post_route)
    return app


# Active apps will have routes automatically generated for them
active_apps = [
    default,
]
