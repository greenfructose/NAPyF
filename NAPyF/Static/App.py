# Define app and routes below

from NAPyF.App import App
from NAPyF.Types import Route, Method


def static(global_static_directory, base_directory):
    app = App('static')
    app.default_route = Route(
        app_name=app.name,
        route_path=app.relative_route_path,
        request_method=Method.GET.value,
        file_path=global_static_directory,
        context=None,
        auth_level_required=0,
    )
    app.add_route(app.default_route)
    return app
