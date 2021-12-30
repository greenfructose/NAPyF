import params as params

from NAPyF.Auth.Models import User, list_users, get_user, update_user
from NAPyF.Auth.Session import Session
from NAPyF.Auth.Models import verify_password


def default_post(form=None, params=None):
    success = False
    return_data = {}
    if form is None:
        print('No form data posted')
    else:
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                return_data = f'Uploaded {field} as "{field_item.filename}" ({file_len} bytes)\n'
            else:
                # Regular form value
                # return_data += '\t%s=%s\n' % (field, form[field].value)
                return_data[field] = form[field].value
        print(return_data)
        user = User()
        user.create_user(**return_data)
        success = True
    return success


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
    print(f'Data: {data}')
    return data['username']


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
    update_user(users_id, data)
    return None


active_functions = {
    'default_post': default_post,
    'auth_post_user': auth_post_user,
    'auth_list_users': auth_list_users,
    'auth_login_user': auth_login_user,
    'auth_logout_user': auth_logout_user,
    'auth_get_user': auth_get_user,
    'auth_update_user': auth_update_user,
}
