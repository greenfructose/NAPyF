from Apps.profile.Models import Profile
from NAPyF.Admin.RequestFunctions import auth_post_user
from NAPyF.DataBase import open_db_connection


def update_profile(id: int, params):

    con = open_db_connection()
    cur = con.cursor()
    sql_update_query = """
    UPDATE profile
    SET
    first_name = ?,
    last_name = ?,
    email = ?,
    username = ?,
    picture = ?,
    bio = ?
    WHERE profile_id = ?
    """
    data = (
        params["first_name"],
        params["last_name"],
        params["email"],
        params["username"],
        params["picture"],
        params["bio"],
        id,
    )
    cur.execute(sql_update_query, data)
    con.commit()
    con.close()
    return


def request_update_profile(form=None, params=None):
    profile_id = params['id']
    data = {}
    for field in form.keys():
        data[field] = form[field].value
    update_profile(profile_id, data)
    return True


def create_user(form=None, params=None):
    if auth_post_user(form, params):
        return True


def get_profile(form=None, params=None):
    con = open_db_connection()
    cur = con.cursor()
    print(params)
    if 'id' in params:
        id = params['id']
        cur.execute("SELECT profile_id, first_name, last_name, email, username, picture, bio from "
                    "profile WHERE profile_id = (?)", [id])
    elif 'username' in params:
        username = params['username']
        cur.execute("SELECT profile_id, first_name, last_name, email, username, picture, bio from "
                    "profile WHERE username = (?)", [username])
    profile = cur.fetchone()
    profile = {
        "profile_id": profile[0],
        "first_name": profile[1],
        "last_name": profile[2],
        "email": profile[3],
        "username": profile[4],
        "picture": profile[5],
        "bio": profile[6],
    }
    con.close()
    return profile

