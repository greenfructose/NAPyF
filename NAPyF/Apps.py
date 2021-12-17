from NAPyF.App import App
from NAPyF.Types import Route, Method


def default():
    app = App('default')
    app.add_route(Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={},
        method=Method.GET
    ))
    return app


active_apps = [
    default,
]
