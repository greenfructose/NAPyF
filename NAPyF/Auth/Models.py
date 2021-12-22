import binascii
import hashlib
import os

from NAPyF.Model import Model
from NAPyF.Types import Field
from NAPyF.DataBase import insert, open_db_connection


class User(Model):
    def __init__(self):
        super().__init__()

    name = 'users'
    fields = [
        Field(
            name='first_name',
            display_name='First Name',
            data_type=str,
            max_length=20,
            data=None
        ),
        Field(
            name='last_name',
            display_name='Last Name',
            data_type=str,
            max_length=20,
            data=None
        ),
        Field(
            name='email',
            display_name='Email Address',
            data_type=str,
            max_length=20,
            data=None
        ),
        Field(
            name='phone_number',
            display_name='Phone Number',
            data_type=str,
            max_length=20,
            data=None
        ),
        Field(
            name='username',
            display_name='Username',
            data_type=str,
            max_length=20,
            data=None
        ),
        Field(
            name='password',
            display_name='Password',
            data_type=str,
            max_length=100,
            data=None
        ),
        Field(
            name='auth_level',
            display_name='Authorization Level',
            data_type=int,
            max_length=4,
            data=0
        ),
        Field(
            name='is_verified',
            display_name='Is Verified',
            data_type=bool,
            max_length=100,
            data=False
        ),
    ]

    def create_user(self, first_name, last_name, email, phone_number, username, password, auth_level, is_verified):
        for field in self.fields:
            if field["name"] == "first_name":
                field["data"] = first_name
            if field["name"] == "last_name":
                field["data"] = last_name
            if field["name"] == "email":
                field["data"] = email
            if field["name"] == "phone_number":
                field["data"] = phone_number
            if field["name"] == "username":
                field["data"] = username
            if field["name"] == "password":
                hashed_password = hash_password(password)
                field["data"] = hashed_password
            if field["name"] == "auth_level":
                field["data"] = auth_level
            if field["name"] == "is_verified":
                field["data"] = is_verified
        con = open_db_connection()
        insert(con, self)
        con.close()


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
    pwd_hash = binascii.hexlify(pwd_hash)
    return (salt + pwd_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwd_hash = hashlib.pbkdf2_hmac('sha512',
                                   provided_password.encode('utf-8'),
                                   salt.encode('ascii'),
                                   100000)
    pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')
    return pwd_hash == stored_password



