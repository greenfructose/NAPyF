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

# Default app name
APP_NAME = 'default'

# Default Project Directories Directories
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = BASE_DIR + f'/{APP_NAME}/base/templates'

# Default file project locations
ROUTES_FILE = BASE_DIR + '/NAPyF/Routes.py'

# App creation templates
APP_INDEX_TEMPLATE = BASE_DIR + '/NAPyF/FileTemplates/index.html'


# Terminal Text Colors
class TermColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
