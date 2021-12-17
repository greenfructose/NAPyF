from NAPyF.Apps import *


def route_builder():
    routes = []
    for app in active_apps:
        temp_app = app()
        for route in temp_app.routes:
            routes.append(route)
    return routes
