from Apps.profile.Models import Profile
from NAPyF.Admin.RequestFunctions import auth_post_user
from NAPyF.DataBase import open_db_connection


# def create_profile(form=None, params=None, user_id=None):
#     data = {}
#     if form is None and params is None:
#         print('No form data posted')
#         return False
#     else:
#         profile = Profile()
#         if form is not None:
#             for field in profile.fields:
#                 if field["name"] == 'profiles_id':
#                     data["profiles_id"] = user_id
#                 if field["name"] in form.keys():
#                     data[field["name"]] = form[field["name"]].value
#             profile.create_profile(**data)
#     return True


def create_user(form=None, params=None):
    if auth_post_user(form, params):
        return True


def get_profile(form=None, params=None):
    con = open_db_connection()
    cur = con.cursor()
    print(params)
    if 'id' in params:
        id = params['id']
        cur.execute("SELECT profile_id, first_name, last_name, email, username, picture from "
                    "profile WHERE profile_id = (?)", [id])
    elif 'username' in params:
        username = params['username']
        cur.execute("SELECT profile_id, first_name, last_name, email, username, picture from "
                    "profile WHERE username = (?)", [username])
    profile = cur.fetchone()
    profile = {
        "profile_id": profile[0],
        "first_name": profile[1],
        "last_name": profile[2],
        "email": profile[3],
        "username": profile[4],
        "picture": profile[5],
    }
    con.close()
    return profile

