import socketserver
from fileinput import filename

from Settings import HTTP_PORT, CURRENT_DIR
from TemplateEngine import render
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class StaticServer(BaseHTTPRequestHandler):
    context = None
    filename = None
    path_filename = {}

    def do_GET(self):
        root = os.path.dirname(os.path.realpath(__file__))
        if self.path not in self.path_filename:
            self.context = {'path': self.path}
            self.filename = root + '/404.html'
        else:
            self.filename = root + path_filename.get(self.path)
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
        # with open(filename, 'rb') as fh:
        #     html = fh.read()
        #     # html = bytes(html, 'utf8')
        #     self.wfile.write(html)


path_filename = {'/': '/index.html', '/boots': '/boots.html'}
context = {'a': 'buffalo'}
server = HTTPServer
handler = StaticServer
handler.context = context
handler.path_filename = path_filename
port = HTTP_PORT


def run(server_class=server, handler_class=handler, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()
