import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
from NAPyF.Routes import routes
from Settings import HTTP_PORT, BASE_DIR
from NAPyF.TemplateEngine import render


class StaticServer(BaseHTTPRequestHandler):
    context = None
    filename = None
    routes = {}

    def do_GET(self):
        root = BASE_DIR
        if self.path not in self.routes:
            self.send_response(404)
            self.context = {'path': self.path}
            self.filename = root + '/error_pages/404.html'
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
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    try:
        print('Starting httpd on port {}'.format(port))
        webbrowser.open('http://' + server_address[0] + ':' + str(server_address[1]))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        httpd.shutdown()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        sys.exit(0)
