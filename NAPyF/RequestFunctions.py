from NAPyF.Auth.Models import User, list_users
from NAPyF.Auth.Session import Session
from NAPyF.Auth.Models import verify_password


def default_post(form=None):
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


def auth_post_user(form=None):
    success = False
    data = {}
    if form is None:
        print('No form data posted')
    else:
        for field in form.keys():
            data[field] = form[field].value
        user = User()
        user.create_user(**data)
        success = True
    return success


def auth_login_user(form=None):
    data = {}
    if form is None:
        print('No data posted to form')
    else:
        for field in form.keys():
            data[field] = form[field].value
        if verify_password(**data):
            session = Session()
            session.sid = session.generate_sid()
            session.cookie = f'sid={session.sid}'
            session.session = {session.sid: {"username", "useragent", "ip address", "expiry"}}
            return session
        else:
            print('Username or password is incorrect')
            return None


def auth_logout_user(form=None):
    if form['user']:
        return form['user']
    else:
        print('User not logged in')


def auth_list_users():
    return list_users()


active_functions = {
    'default_post': default_post,
    'auth_post_user': auth_post_user,
    'auth_list_users': auth_list_users,
    'auth_login_user': auth_login_user,
}
