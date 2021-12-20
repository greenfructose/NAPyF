import sys
from http.server import BaseHTTPRequestHandler
from NAPyF.App import App
from NAPyF.active_routes import routes
from NAPyF.Types import Method
from NAPyF.TemplateEngine import render
from Settings import BASE_DIR


class RequestHandler(BaseHTTPRequestHandler):
    app = None
    context = None
    file_path = None
    route = None
    route_path = None
    route_match = False

    def do_GET(self):
        # self.set_app()
        # self.get_route_paths(self.app)
        if self.path == "/killserver":
            print('Closing the server...')
            self.server.server_close()
            print('Server closed, exiting now')
            sys.exit()
        root = BASE_DIR
        self.match_route(Method.GET.value)
        if not self.route_match:
            self.send_response(404)
            self.context = {'path': self.path}
            self.file_path = root + '/NAPyF/FileTemplates/error_pages/404.html'
        else:
            # self.set_filepath_context(Method.GET.value)
            self.send_response(200)
        if self.file_path[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif self.file_path[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif self.file_path[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif self.file_path[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str.encode(render(self.file_path, self.context)))

    def match_route(self, method):
        for route in routes:
            if self.path == route["route_path"] and method == route["method"]:
                print('Route match!')
                self.route_match = True
                self.file_path = route["file_path"]
                self.context = route["context"]

    # def get_route_paths(self, app):
    #     for route in routes:
    #         if route["app_name"] == app.name:
    #             print(f'Adding route {route["route_path"]} to request')
    #             self.route_paths.append(route["route_path"])

    # def set_app(self):
    #     for route in routes:
    #         if self.path == route["route_path"]:
    #             self.app = App(route["app_name"])
    #             print(f'App is {self.app.name}')
    #             self.route_paths.append(route)
    #             print(f'Route paths : {self.route_paths}')
    #         else:
    #             self.app = App('default')
    #
    # def set_filepath_context(self, method):
    #     for route in routes:
    #         if self.path == route["route_path"] and method == route["method"]:
    #             print(f'Route match! Serving {route["file_path"]}')
    #             self.file_path = route["file_path"]
    #             self.context = route["context"]
