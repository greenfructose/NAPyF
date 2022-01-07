
import sys
import mimetypes
from http.server import BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from importlib import reload
from urllib import parse
import NAPyF.active_routes
from NAPyF.Types import Method
from NAPyF.TemplateEngine import render
from NAPyF.RequestFunctions import active_functions
from NAPyF.Admin.Auth.Session import Session
from NAPyF.Admin.Auth.AuthFunctions import auth_level
import NAPyF.Routes as Route
import cgi
from Settings import GLOBAL_STATIC_DIRECTORY, BASE_DIR
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
            self.server.server_close()
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
                mimetype = mimetypes.guess_type(self.file_path)[0]
                self.send_header('Content-Type', mimetype)
                if not mimetype == 'text/html':
                    self.end_headers()
                    with open(self.file_path, 'rb') as f:
                        self.wfile.write(f.read())
                    return
                self.end_headers()
                if 'request_function' in self.route:
                    result = active_functions[self.route["request_function"]](params)
                    self.context = self.context | result
                if self.session is None:
                    self.session = Session()
                self.wfile.write(str.encode(render(self.file_path, self.context, self.session)))
                return

    def do_POST(self):
        global sessions
        path = parse.urlsplit(self.path).path
        params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        authorized = 0
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
        if isinstance(result, Session):
            self.session = result
        if self.session:
            self.session.session['useragent'] = self.headers['User-Agent']
            self.session.session['ip_address'] = self.address_string()
            if self.session.sid not in sessions:
                sessions = sessions | {self.session.sid: self.session.session}
            authorized = auth_level(self.session.session['username'])

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
            if type(result) == dict:
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
                    Route.route_builder(GLOBAL_STATIC_DIRECTORY, BASE_DIR)
                    self.send_response(302)
                    if self.session:
                        if self.session.cookie != {}:
                            self.send_header('Set-Cookie', self.session.cookie)
                    self.send_header('Location', self.route["redirect"])
                    self.end_headers()
                    return
                else:
                    Route.route_builder(GLOBAL_STATIC_DIRECTORY, BASE_DIR)
                    self.send_response(200)
                    self.context = self.context | params
                    if self.session:
                        if self.session.cookie != {}:
                            self.send_header('Set-Cookie', self.session.cookie)
                    self.end_headers()
                    self.wfile.write(result)
                    return

    def match_route(self, method, path):
        # Route.route_builder()
        for route in NAPyF.active_routes.routes:
            if '/static' in route["route_path"] and '/static' in path:
                self.route_match = True
                path = path.replace('/static', '')
                self.file_path = route["file_path"] + path
                self.route = route
                return
            elif path == route["route_path"] and method == route["request_method"]:
                self.route_match = True
                # self.app = App(route["app_name"])
                self.file_path = route["file_path"]
                self.context = route["context"]
                self.context["html_templates"] = route["html_templates"]
                self.route = route
                return
