# Settings for server and DB connections
import os
from NAPyF.Types import ServerMode

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
TEMPLATE_DIR = BASE_DIR + f'/default/base/templates'

# Default file project locations
ROUTE_FILE = BASE_DIR + ' /NAPyF/Routes'
ROUTES_FILE = BASE_DIR + '/NAPyF/active_routes.py'
APPS_FILE = BASE_DIR + '/NAPyF/Apps.py'

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


class CodeFormatOptions(object):
    def __init__(self):
        self.in_place = True
        self.pep8_passes = 1
        self.list_fixes = None
        self.jobs = 1
        self.ignore = []
        self.verbose = 0
        self.diff = None
        self.select = []
        self.exclude = []
        self.aggressive = 2
        self.line_range = []
        self.recursive = None
        self.max_line_length = 79
        self.indent_size = 4
        self.experimental = False
        self.hang_closing = True


CODE_FORMAT_OPTIONS = CodeFormatOptions()
