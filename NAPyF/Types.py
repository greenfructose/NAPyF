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
    def __init__(self, app_name, route_path, file_path, request_method, context):
        self.app_name = app_name
        self.route_path = route_path
        self.request_method = request_method
        self.file_path = file_path
        self.context = context

    request_function = None
    html_templates = {}


class Field(TypedDict):
    name: str
    display_name: str
    data_type: Type
    max_length: int
    data: Any
    visible: bool
