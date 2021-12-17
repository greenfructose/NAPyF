# Custom Data Types
from typing import TypedDict
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
class Route(TypedDict):
    app_name: str
    route_path: str
    file_path: str
    context: dict
    method: Method
