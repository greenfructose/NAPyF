# Settings for server and DB connections
import os
from Types import ServerMode

# Set mode to DEV or PROD
MODE = ServerMode.DEV.name
if MODE == "DEV":
    HTTP_PORT = 8080
    HTTPS_PORT = 8443


if MODE == "PROD":
    HTTP_PORT = 80
    HTTPS_PORT = 443

# Directory of running file
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
