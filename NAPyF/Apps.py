from NAPyF.App import App
from NAPyF.Types import Route, Method


def default():
    app = App('default')
    app.add_route(Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        method=Method.GET.value
    ))
    return app


def test():
    app = App('test')
    return app


def test1():
    app = App('test1')
    return app


active_apps = [
    default,
    test,
    test1,
]
