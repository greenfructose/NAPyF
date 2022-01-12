from Apps.profile.Models import Profile
from NAPyF.Admin.RequestFunctions import auth_post_user
from NAPyF.DataBase import open_db_connection
from Settings import APPS_DIR


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


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


def get_profile_id_by_username(username):
    con = open_db_connection()
    cur = con.cursor()
    query = """
    SELECT profile_id FROM profile WHERE username = (?)
    """
    cur.execute(query, [username])
    return cur.fetchone()[0]


def request_update_profile(form=None, params=None):
    profile_id = params['id']
    username = params['username']
    if profile_id == get_profile_id_by_username(username):
        data = {}
        for field in form.keys():
            if field == 'picture':
                fileitem = form["picture"]
                data[field] = fileitem.file.read()
            else:
                data[field] = form[field].value
        update_profile(profile_id, data)
        return True
    else:
        return False


def create_user(form=None, params=None):
    if auth_post_user(form, params):
        return True


def write_to_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


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
    write_to_file(profile[5], f'{APPS_DIR}/profile/local_static/profiles/{profile[0]}_profile_picture.png')
    profile = {
        "profile_id": profile[0],
        "first_name": profile[1],
        "last_name": profile[2],
        "email": profile[3],
        "username": profile[4],
        "picture": f'{profile[0]}_profile_picture.png',
        "bio": profile[6],
    }
    con.close()
    return profile
