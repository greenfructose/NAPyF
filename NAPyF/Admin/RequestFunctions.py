from pprint import pprint

from NAPyF.Admin.Auth.Models import User
from NAPyF.Admin.Auth.Session import Session
from NAPyF.Admin.Auth.AuthFunctions import verify_password, list_users, get_user, update_user, delete_user
from NAPyF.DataBase import open_db_connection


def auth_post_user(form=None, params=None):
    data = {}
    if form is None and params is None:
        print('No form data posted')
        return None
    else:
        user = User()
        if form is not None:
            for field in form.keys():
                data[field] = form[field].value
            user.create_user(**data)
        if params is not None:
            user.create_user(**params)
        return user.id


def auth_login_user(form=None, params=None):
    data = {}
    if form is None:
        print('No data posted to form')
    else:
        for field in form.keys():
            data[field] = form[field].value
        if verify_password(**data):
            session = Session()
            session.cookie = f'sid={session.sid}; Max-Age=43200; Path=/; HttpOnly'
            session.session = {
                "username": data['username'],
                "useragent": '',
                "ip_address": '',
            }
            return session
        else:
            print('Username or password is incorrect')
    return False


def auth_logout_user(form=None, params=None):
    data = {}
    for field in form.keys():
        data[field] = form[field].value
    result = {'username': data['username'], 'logout': True}

    return result


def list_profiles():
    profiles = []
    con = open_db_connection()
    cur = con.cursor()
    try:
        cur.execute("SELECT profiles_id, first_name, last_name, email, username, picture from "
                    "profiles")
        for row in cur.fetchall():
            profiles.append({
                "profiles_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "username": row[4],
                "picture": row[5],
            })
    except Exception as e:
        print(f'The following error occurred:\n{e}')
    return profiles


def auth_list_admin_objects():
    admin_objects = {
        'admin-user': list_users(),
        'profile': list_profiles()
    }
    return admin_objects


def auth_get_user(params):
    # print(f'Kwargs: {**kwargs}')
    db_user = get_user(params['id'])
    user = {
        'id': db_user[0],
        'first_name': db_user[1],
        'last_name': db_user[2],
        'email': db_user[3],
        'username': db_user[4],
        'password': "",
        'auth_level': db_user[5],
        'is_verified': db_user[6]
    }
    return user


def auth_update_user(form=None, params=None):
    users_id = params['id']
    data = {}
    for field in form.keys():
        data[field] = form[field].value
    if 'is_verified' not in data:
        data['is_verified'] = False
    else:
        data['is_verified'] = True
    update_user(users_id, data)
    return True


def auth_delete_user(form=None, params=None):
    users_id = params['id']
    delete_user(users_id)
    return True


def get_sessions(form=None, params=None):
    from NAPyF.RequestHandler import sessions
    session_dict = {'sessions': sessions}
    return session_dict


active_functions = {
    'auth_post_user': auth_post_user,
    'auth_list_admin_objects': auth_list_admin_objects,
    'auth_login_user': auth_login_user,
    'auth_logout_user': auth_logout_user,
    'auth_get_user': auth_get_user,
    'auth_update_user': auth_update_user,
    'auth_delete_user': auth_delete_user,
    'get_sessions': get_sessions,
}
