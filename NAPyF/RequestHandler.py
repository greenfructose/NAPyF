import sys
from http.server import BaseHTTPRequestHandler
from NAPyF.Apps import default
from NAPyF.App import App
from NAPyF.Routes import routes
from NAPyF.TemplateEngine import render
from Settings import BASE_DIR


class RequestHandler(BaseHTTPRequestHandler):
    app = None
    context = None
    filename = None
    routes = {}

    def do_GET(self):
        root = BASE_DIR
        if self.path not in self.routes:
            if self.path == "/killserver":
                print('Closing the server...')
                self.server.server_close()
                print('Server closed, exiting now')
                sys.exit()
            self.send_response(404)
            self.context = {'path': self.path}
            self.filename = root + '/NAPyF/FileTemplates/error_pages/404.html'
        else:
            self.app = App(root + routes.get(self.path))
            self.filename = root + routes.get(self.path)
            self.send_response(200)
        if self.filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif self.filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif self.filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif self.filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str.encode(render(self.filename, self.context)))