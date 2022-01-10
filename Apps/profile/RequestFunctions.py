from Apps.profile.Models import Profile
from NAPyF.Admin.RequestFunctions import auth_post_user
from NAPyF.DataBase import open_db_connection


def create_profile(form=None, params=None, user_id=None):
    data = {}
    if form is None and params is None:
        print('No form data posted')
        return False
    else:
        profile = Profile()
        if form is not None:
            for field in profile.fields:
                if field["name"] == 'profiles_id':
                    data["profiles_id"] = user_id
                if field["name"] in form.keys():
                    data[field["name"]] = form[field["name"]].value
            profile.create_profile(**data)
    return True


def create_user(form=None, params=None):
    users_id = auth_post_user(form, params)
    create_profile(form, params, users_id)
    return True


def get_profile(form=None, params=None):
    con = open_db_connection()
    cur = con.cursor()
    cur.execute("SELECT profiles_id, first_name, last_name, email, username, picture from "
                "profiles WHERE profiles_id = (?)", [params['id']])
    profile = cur.fetchone()
    profile = {
        "profiles_id": profile[0],
        "first_name": profile[1],
        "last_name": profile[2],
        "email": profile[3],
        "username": profile[4],
        "picture": profile[5],
    }
    return profile
