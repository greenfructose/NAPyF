from pathlib import Path
from pprint import pprint
import autopep8

import Settings
from NAPyF.Apps import active_apps
from Settings import ROUTES_FILE, CODE_FORMAT_OPTIONS


def route_builder():
    routes = []
    for app in active_apps:
        temp_app = app()
        for route in temp_app.routes:
            pprint(route)
            routes.append(route)
    with open(ROUTES_FILE, 'w+') as f:
        f.write('from NAPyF.Types import Method\n'
                f'routes = {routes}')
    autopep8.fix_file(ROUTES_FILE, CODE_FORMAT_OPTIONS)
