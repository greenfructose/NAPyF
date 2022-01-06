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

# Default Project Directories
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
APPS_DIR = BASE_DIR + '/Apps'
# Global Static Directory
GLOBAL_STATIC_DIRECTORY = BASE_DIR + '/global_static'

# Default file project locations
ROUTE_FILE = BASE_DIR + ' /NAPyF/Routes'
ROUTES_FILE = BASE_DIR + '/NAPyF/active_routes.py'
APPS_FILE = BASE_DIR + '/NAPyF/Apps.py'
ACTIVE_APPS_FILE = BASE_DIR + '/ActiveApps.py'

# App creation templates
APP_INDEX_TEMPLATE = BASE_DIR + '/NAPyF/FileTemplates/index.html'

# Database Settings
DB_TYPE = 'sqlite3'


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


# Settings for the autopep8 code formatter
class CodeFormatOptions(object):
    def __init__(self):
        self.in_place = True
        self.pep8_passes = -1
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
        self.hang_closing = False


CODE_FORMAT_OPTIONS = CodeFormatOptions()

USERNAME_REQS = r'^[A-Za-z0-9]+$'
USERNAME_ERROR_TEXT = 'Letters and numbers only, no punctuation or special characters.'

NAME_REQS = r'^[a-zA-Z]+$'
NAME_ERROR_TEXT = 'Letters only, no numbers, punctuation or special characters.'

EMAIL_REQS = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
EMAIL_ERROR_TEXT = 'Please enter a valid email address.'

PASSWORD_REQS = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
PASSWORD_ERROR_TEXT = "Password must be at least 8 characters long with at least one uppercase ' \
                          'letter, one lowercase letter, one number, and one special character (@$!%*?&). "