from importlib import reload
from pathlib import Path
from pprint import pprint
import autopep8

import Settings
import NAPyF.Apps
from Settings import ROUTES_FILE, CODE_FORMAT_OPTIONS


def route_builder():
    routes = []
    reload(NAPyF.Apps)
    for app in NAPyF.Apps.active_apps:
        temp_app = app()
        for route in temp_app.routes:
            pprint(route)
            routes.append(route)
    new_routes_string = ('from NAPyF.Types import Method\n'
                         f'routes = {routes}')
    new_routes_string = autopep8.fix_code(new_routes_string, CODE_FORMAT_OPTIONS)
    with open(ROUTES_FILE, 'w+') as f:
        f.write(new_routes_string)
    # autopep8.fix_file(ROUTES_FILE, CODE_FORMAT_OPTIONS)
