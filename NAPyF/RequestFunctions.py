from NAPyF.Admin.RequestFunctions import *
from Apps.default.RequestFunctions import *
from Apps.profile.RequestFunctions import *

active_functions = {
    'auth_post_user': auth_post_user,
    'auth_list_users': auth_list_users,
    'auth_login_user': auth_login_user,
    'auth_logout_user': auth_logout_user,
    'auth_get_user': auth_get_user,
    'auth_update_user': auth_update_user,
    'auth_delete_user': auth_delete_user,
}