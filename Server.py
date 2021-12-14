from Routes import routes
from Settings import HTTP_PORT, CURRENT_DIR
from TemplateEngine import render
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class StaticServer(BaseHTTPRequestHandler):
    context = None
    filename = None
    routes = {}

    def do_GET(self):
        root = os.path.dirname(os.path.realpath(__file__))
        if self.path not in self.routes:
            self.send_response(404)
            self.context = {'path': self.path}
            self.filename = root + '/404.html'
        else:
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

# testing stuff
context = {'a': 'buffalo'}
server = HTTPServer
handler = StaticServer
handler.context = context
handler.routes = routes
port = HTTP_PORT


def run(server_class=server, handler_class=handler, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()
