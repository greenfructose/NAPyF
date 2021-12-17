import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
from Settings import HTTP_PORT, BASE_DIR
from NAPyF.RequestHandler import RequestHandler

# testing stuff
server = HTTPServer
handler = RequestHandler
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
