import sys
from http.server import HTTPServer
import webbrowser
from Settings import HTTP_PORT, GLOBAL_STATIC_DIRECTORY, BASE_DIR
from NAPyF.RequestHandler import RequestHandler
from NAPyF.Routes import route_builder
from socketserver import ThreadingMixIn


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


handler = RequestHandler
server = ThreadedHTTPServer(('localhost', HTTP_PORT), handler)


def run():
    server_address = ('localhost', HTTP_PORT)
    print('Setting routes...')
    route_builder(GLOBAL_STATIC_DIRECTORY, BASE_DIR)
    httpd = server
    try:
        print('Starting httpd on port {}'.format(HTTP_PORT))
        webbrowser.open('http://' + server_address[0] + ':' + str(server_address[1]))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        httpd.shutdown()
    return


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        sys.exit(0)
