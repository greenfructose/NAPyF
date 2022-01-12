# Custom Data Types
from typing import TypedDict, Any, Type
from enum import Enum


# Server mode for switching settings
class ServerMode(Enum):
    DEV = 1
    PROD = 2


# HTTP methods
class Method(Enum):
    GET = 1
    POST = 2
    PUT = 3


# Route TypedDict, route_path is url, file_path is file location to server at route
class Route(object):
    def __init__(self, app_name, route_path, file_path, request_method, context, auth_level_required):
        self.app_name = app_name
        self.route_path = route_path
        self.request_method = request_method
        self.file_path = file_path
        self.context = context
        self.auth_level_required = auth_level_required

    request_function = None
    html_templates = {}
    redirect = None


class ForeignKey(object):
    def __init__(self, local_key, referenced_table, referenced_key):
        self.local_key = local_key
        self.referenced_table = referenced_table
        self.referenced_key = referenced_key
        if self.local_key is not None:
            self.key_string = self.get_key_string()

    def get_key_string(self):
        return f'FOREIGN KEY ({self.local_key}) REFERENCES {self.referenced_table}({self.referenced_key}), '


class Field(TypedDict, total=False):
    name: str
    display_name: str
    data_type: Type
    max_length: int
    data: Any
    visible: bool
    foreign_key: ForeignKey
    filename: str
