from NAPyF.Admin.Auth.Models import User
from NAPyF.Admin.Auth.Session import Session
from NAPyF.Admin.Auth.AuthFunctions import verify_password, list_users, get_user, update_user, delete_user


def auth_post_user(form=None, params=None):
    data = {}
    if form is None:
        print('No form data posted')
        return None
    else:
        for field in form.keys():
            data[field] = form[field].value
        user = User()
        user.create_user(**data)
    return True


def auth_login_user(form=None, params=None):
    data = {}
    if form is None:
        print('No data posted to form')
    else:
        for field in form.keys():
            data[field] = form[field].value
        if verify_password(**data):
            session = Session()
            session.generate_sid()
            session.cookie = f'sid={session.sid}; Max-Age=43200; Path=/; HttpOnly'
            session.session = {
                session.sid: {
                    "username": data['username'],
                    "useragent": '',
                    "ip_address": '',
                }
            }
            return session
        else:
            print('Username or password is incorrect')
    return None


def auth_logout_user(form=None, params=None):
    data = {}
    for field in form.keys():
        data[field] = form[field].value
    result = {'username': data['username'], 'logout': True}
    return result


def auth_list_users():
    return list_users()


def auth_get_user(params):
    # print(f'Kwargs: {**kwargs}')
    db_user = get_user(params['id'])
    user = {
        'id': db_user[0],
        'first_name': db_user[1],
        'last_name': db_user[2],
        'email': db_user[3],
        'phone_number': db_user[4],
        'username': db_user[5],
        'password': "",
        'auth_level': db_user[6],
        'is_verified': db_user[7]
    }
    return user


def auth_update_user(form=None, params=None):
    users_id = params['id']
    data = {}
    for field in form.keys():
        data[field] = form[field].value
    print(f"Data: {data}")
    if 'is_verified' not in data:
        data['is_verified'] = False
    else:
        data['is_verified'] = True
    update_user(users_id, data)
    return None


def auth_delete_user(form=None, params=None):
    users_id = params['id']
    delete_user(users_id)
    return None


active_functions = {
    'auth_post_user': auth_post_user,
    'auth_list_users': auth_list_users,
    'auth_login_user': auth_login_user,
    'auth_logout_user': auth_logout_user,
    'auth_get_user': auth_get_user,
    'auth_update_user': auth_update_user,
    'auth_delete_user': auth_delete_user,
}
