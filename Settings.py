# Settings for server and DB connections
import os
from NAPyF.Types import ServerMode
from NAPyF.Routes import routes

# Set mode to DEV or PROD
MODE = ServerMode.DEV.name
if MODE == "DEV":
    HTTP_PORT = 8080
    HTTPS_PORT = 8443


if MODE == "PROD":
    HTTP_PORT = 80
    HTTPS_PORT = 443

# Default Project Directories Directories
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = BASE_DIR + '/default/base/templates'

# Default file project locations
ROUTES_FILE = BASE_DIR + '/NAPyF/Routes.py'

# App creation templates
APP_INDEX_TEMPLATE = BASE_DIR + '/NAPyF/FileTemplates/index.html'

