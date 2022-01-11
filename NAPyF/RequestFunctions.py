from NAPyF.Admin.RequestFunctions import *
from Apps.default.RequestFunctions import *
from Apps.profile.RequestFunctions import *

active_functions = {
    'auth_post_user': auth_post_user,
    'auth_list_admin_objects': auth_list_admin_objects,
    'auth_login_user': auth_login_user,
    'auth_logout_user': auth_logout_user,
    'auth_get_user': auth_get_user,
    'auth_update_user': auth_update_user,
    'auth_delete_user': auth_delete_user,
    'get_sessions': get_sessions,
    'create_user': create_user,
    'get_profile': get_profile,
    'request_update_profile': request_update_profile,
}