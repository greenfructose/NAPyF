import sys
import inspect
from http.server import BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from importlib import reload
from urllib import parse
import NAPyF.active_routes
from NAPyF.App import App
from NAPyF.Types import Method
from NAPyF.TemplateEngine import render
from NAPyF.RequestFunctions import active_functions
from NAPyF.Admin.Auth.Session import Session
from NAPyF.Admin.Auth.AuthFunctions import auth_level
import NAPyF.Routes as Route
from Settings import BASE_DIR
import cgi

sessions = {}


class RequestHandler(BaseHTTPRequestHandler):
    app = None
    context = {}
    file_path = None
    route = None
    route_path = None
    route_match = False
    route_authorized = False
    request_function = None
    session = None
    user_session = None

    def do_GET(self):
        reload(NAPyF.active_routes)
        path = parse.urlparse(self.path).path
        params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        global sessions
        authorized = 0
        print(self.headers)
        if self.headers['Cookie'] is not None:
            raw_data = self.headers['Cookie']
            cookie = SimpleCookie()
            cookie.load(raw_data)
            cookies = {}
            for key, morsel in cookie.items():
                cookies[key] = morsel.value
            if "sid" in cookies:
                if cookies["sid"] in sessions:
                    self.session = Session()
                    self.session.sid = cookies["sid"]
                    self.session.user = sessions[self.session.sid]['username']
                    authorized = auth_level(self.session.user)
        if path == "/showsessions":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str.encode(str(sessions)))
            return

        if path == "/killserver":
            print('Closing the server...')
            self.server.server_close()
            print('Server closed, exiting now')
            sys.exit()
        self.match_route(Method.GET.value, path)
        if not self.route_match:
            self.send_response(404)
            self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/404.html'
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str.encode(render(self.file_path, {'path': path}, self.session)))
            return

        else:
            if authorized >= self.route['auth_level_required']:
                self.route_authorized = True
            if not self.route_authorized:
                self.send_response(401)
                self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/401.html'
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str.encode(render(self.file_path, {'path': path}, self.session)))
                return
            else:
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
                if 'request_function' in self.route:
                    result = active_functions[self.route["request_function"]](params)
                    self.context = self.context | result
                self.wfile.write(str.encode(render(self.file_path, self.context, self.session)))
                return

    def do_POST(self):
        global sessions
        path = parse.urlsplit(self.path).path
        print(f'Path: {path}')
        params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        authorized = 0
        print(f'Headers:\n{self.headers}')
        reload(NAPyF.active_routes)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )
        self.match_route(Method.POST.value, path)
        result = active_functions[self.route["request_function"]](form=form, params=params)
        if inspect.isclass(result):
            if result.is_session:
                self.session = result
        if self.session:
            print(f'Headers: \n {self.headers}')
            self.session.session[self.session.sid]['useragent'] = self.headers['User-Agent']
            self.session.session[self.session.sid]['ip_address'] = self.address_string()
            if self.session.sid not in sessions:
                sessions = sessions | self.session.session
                self.session.cookie = f'sid={self.session.sid}'
            authorized = auth_level(self.session.session[self.session.sid]['username'])
        elif self.headers['Cookie'] is not None:
            raw_data = self.headers['Cookie']
            cookie = SimpleCookie()
            cookie.load(raw_data)
            cookies = {}
            for key, morsel in cookie.items():
                cookies[key] = morsel.value
            if "sid" in cookies:
                if cookies["sid"] in sessions:
                    self.session = Session()
                    self.session.sid = cookies["sid"]
                    self.session.user = sessions[self.session.sid]['username']
                    authorized = auth_level(self.session.user)
        if authorized >= self.route['auth_level_required']:
            self.route_authorized = True
        if not self.route_authorized:
            self.send_response(401)
            self.context = {'path': path}
            self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/401.html'
            return
        else:
            if 'logout' in result:
                self.send_response(302)
                username = result['username']
                session_list = []
                for key, value in sessions.items():
                    if value['username'] == username:
                        session_list.append(key)
                for session in session_list:
                    del sessions[session]
                self.send_header('Location', self.route["redirect"])
                self.end_headers()
                return
            else:
                if not self.route_match:
                    self.send_response(404)
                    self.context = {'path': path}
                    self.file_path = BASE_DIR + '/NAPyF/FileTemplates/error_pages/404.html'
                    return
                if self.route["redirect"]:
                    Route.route_builder()
                    self.send_response(302)
                    if self.session.cookie != {}:
                        self.send_header('Set-Cookie', self.session.cookie)
                    self.send_header('Location', self.route["redirect"])
                    self.end_headers()
                    return
                else:
                    Route.route_builder()
                    self.send_response(200)
                    self.context = self.context | params
                    if self.session.cookie != {}:
                        self.send_header('Set-Cookie', self.session.cookie)
                    self.end_headers()
                    self.wfile.write(result)
                    return

    def match_route(self, method, path):
        # Route.route_builder()
        for route in NAPyF.active_routes.routes:
            if path == route["route_path"] and method == route["request_method"]:
                print('Route match!')
                self.route_match = True
                self.app = App(route["app_name"])
                self.file_path = route["file_path"]
                self.context = route["context"]
                self.context["html_templates"] = route["html_templates"]
                self.route = route
        return

