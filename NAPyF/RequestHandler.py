import sys
from http.server import BaseHTTPRequestHandler
from importlib import reload
import datetime
import NAPyF.active_routes
from NAPyF.App import App
from NAPyF.Types import Method
from NAPyF.TemplateEngine import render
from NAPyF.RequestFunctions import active_functions
from NAPyF.Auth.Session import Session
import NAPyF.Routes as Route
from Settings import BASE_DIR
import cgi

sessions = {}


class RequestHandler(BaseHTTPRequestHandler):
    app = None
    context = None
    file_path = None
    route = None
    route_path = None
    route_match = False
    request_function = None
    session = None
    user_session = None

    def do_GET(self):
        global sessions
        reload(NAPyF.active_routes)
        self.session = Session()
        print(self.headers)
        # self.set_app()
        # self.get_route_paths(self.app)
        if self.path == "/showsessions":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str.encode(str(sessions)))
            return

        if self.path == "/killserver":
            print('Closing the server...')
            self.server.server_close()
            print('Server closed, exiting now')
            sys.exit()
        self.match_route(Method.GET.value)
        if not self.route_match:
            self.send_response(404)
            self.context = {'path': self.path}
            self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/404.html'
        else:
            # self.set_filepath_context(Method.GET.value)
            self.send_response(200)
            cookies = self.parse_cookies(self.headers['Cookie'])
            print(f'Cookies: \n {cookies}')
            if "sid" in cookies:
                if cookies["sid"] in sessions:
                    self.session.cookie = cookies["sid"]
            else:
                self.session.cookie = None
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
            if self.session.cookie:
                self.send_header('Set-Cookie', f'sid={self.session.cookie}')
                self.session.user = sessions[self.session.cookie]['username']
                print(sessions[self.session.cookie]['username'])
        self.end_headers()
        self.wfile.write(str.encode(render(self.file_path, self.context, self.session)))
        return

    def do_POST(self):
        global sessions

        print(f'Headers:\n{self.headers}')
        reload(NAPyF.active_routes)
        self.match_route(Method.POST.value)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )
        if not self.route_match:
            self.send_response(404)
            self.context = {'path': self.path}
            self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/404.html'
        if self.route["redirect"]:
            self.session = active_functions[self.route["request_function"]](form=form)
            if self.session:
                self.session.session[self.session.sid]['useragent'] = self.headers['User-Agent']
                expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
                self.session.session[self.session.sid]['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
                self.session.session[self.session.sid]['ip_address'] = self.address_string()
                sessions = sessions | self.session.session
                self.session.cookie = f"sid={self.session.sid}"
            Route.route_builder()
            self.send_response(302)
            self.send_header('Set-Cookie', self.session.cookie)
            self.send_header('Location', self.route["redirect"])
            self.end_headers()
        else:
            Route.route_builder()
            self.send_response(200)
            self.send_header('Set-Cookie', self.session.cookie)
            self.end_headers()
            self.wfile.write(active_functions[self.route["request_function"]](form=form))
            return

    def match_route(self, method):
        for route in NAPyF.active_routes.routes:
            if self.path == route["route_path"] and method == route["request_method"]:
                print('Route match!')
                self.route_match = True
                self.app = App(route["app_name"])
                self.file_path = route["file_path"]
                self.context = route["context"]
                self.context["html_templates"] = route["html_templates"]
                self.route = route
        return

    def parse_cookies(self, cookie_list):
        return dict(((c.split("=")) for c in cookie_list.split(";"))) if cookie_list else {}
