from importlib import reload
import autopep8
from Settings import ROUTES_FILE, CODE_FORMAT_OPTIONS, ACTIVE_APPS, GLOBAL_STATIC_DIRECTORY


def route_builder(global_static_directory):
    """Builds routes based on active apps, removes inactive routes"""
    routes = []
    reload(ACTIVE_APPS)
    for app in ACTIVE_APPS:
        temp_app = app(global_static_directory)
        for route in temp_app.routes:
            routes.append(route)

    new_routes_string = f'routes = {routes}'
    new_routes_string = autopep8.fix_code(new_routes_string, CODE_FORMAT_OPTIONS)
    with open(ROUTES_FILE, 'w+') as f:
        f.write(new_routes_string)
