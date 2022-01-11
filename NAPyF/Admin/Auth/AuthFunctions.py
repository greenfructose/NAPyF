import binascii
import hashlib
import os
from pprint import pprint

from NAPyF.DataBase import open_db_connection


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
    pwd_hash = binascii.hexlify(pwd_hash)
    return (salt + pwd_hash).decode('ascii')


def verify_password(**kwargs):
    """Verify a stored password against one provided by user"""
    username = kwargs['username']
    provided_password = kwargs['password']
    con = open_db_connection()
    cur = con.cursor()
    cur.execute('SELECT password FROM user WHERE username = (?);', [username])
    stored_password = cur.fetchone()[0]
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwd_hash = hashlib.pbkdf2_hmac('sha512',
                                   provided_password.encode('utf-8'),
                                   salt.encode('ascii'),
                                   100000)
    pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')
    con.close()
    return pwd_hash == stored_password


def list_users():
    """List of users in DataBase"""
    user_list = []
    con = open_db_connection()
    cur = con.cursor()
    cur.execute("SELECT user_id, first_name, last_name, email, username, auth_level, is_verified from "
                "user")
    for row in cur.fetchall():
        user_list.append({
            "user_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "username": row[4],
            "auth_level": row[5],
            "is_verified": row[6],
        })
    return user_list


def get_user(id: int):
    con = open_db_connection()
    cur = con.cursor()
    cur.execute("SELECT user_id, first_name, last_name, email, username, auth_level, is_verified from "
                "user WHERE user_id = (?)", [id])
    return cur.fetchone()


def update_user(id: int, params):
    con = open_db_connection()
    cur = con.cursor()
    if 'password' not in params:
        sql_update_query = """
        UPDATE user
        SET
        first_name = ?,
        last_name = ?,
        email = ?,
        username = ?,
        auth_level = ?,
        is_verified = ?
        WHERE user_id = ?
        """
        data = (
            params["first_name"],
            params["last_name"],
            params["email"],
            params["username"],
            params["auth_level"],
            params["is_verified"],
            id,
        )
    else:
        password = hash_password(params["password"])
        sql_update_query = """
        UPDATE user
        SET
        first_name = ?,
        last_name = ?,
        email = ?,
        username = ?,
        password = ?,
        auth_level = ?,
        is_verified = ?
        WHERE user_id = ?
        """
        data = (
            params["first_name"],
            params["last_name"],
            params["email"],
            params["username"],
            password,
            params["auth_level"],
            params["is_verified"],
            id,
        )
    cur.execute(sql_update_query, data)
    con.commit()
    con.close()
    return


def delete_user(id: int):
    sql_delete_query = """
    DELETE FROM user WHERE user_id = (?);
    """
    con = open_db_connection()
    cur = con.cursor()
    cur.execute(sql_delete_query, (id,))
    con.commit()
    con.close()


def auth_level(username=None):
    if username is None:
        return 0
    else:
        con = open_db_connection()
        cur = con.cursor()
        cur.execute("SELECT auth_level FROM user WHERE username = (?);", [username])
        return int(cur.fetchone()[0])
