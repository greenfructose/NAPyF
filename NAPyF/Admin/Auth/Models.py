from pprint import pprint

from NAPyF.Model import Model
from NAPyF.Types import Field
from NAPyF.DataBase import insert, open_db_connection
from NAPyF.Admin.Auth.AuthFunctions import hash_password
from Apps.profile.Models import Profile


class User(Model):
    def __init__(self):
        super().__init__()
    name = 'user'
    fields = [
        Field(
            name='first_name',
            display_name='First Name',
            data_type=str,
            max_length=20,
            data=None,
            visible=True
        ),
        Field(
            name='last_name',
            display_name='Last Name',
            data_type=str,
            max_length=20,
            data=None,
            visible=True
        ),
        Field(
            name='email',
            display_name='Email Address',
            data_type=str,
            max_length=20,
            data=None,
            visible=True
        ),
        Field(
            name='username',
            display_name='Username',
            data_type=str,
            max_length=20,
            data=None,
            visible=True
        ),
        Field(
            name='password',
            display_name='Password',
            data_type=str,
            max_length=32,
            data=None,
            visible=True
        ),
        Field(
            name='auth_level',
            display_name='Authorization Level',
            data_type=int,
            max_length=4,
            data=0,
            visible=False
        ),
        Field(
            name='is_verified',
            display_name='Is Verified',
            data_type=bool,
            max_length=100,
            data=False,
            visible=False
        ),
    ]

    def create_user(self, **kwargs):
        for key, value in kwargs.items():
            for field in self.fields:
                if field["name"] == key:
                    field["data"] = kwargs[key]
                if field["name"] == 'password':
                    hashed_password = hash_password(kwargs["password"])
                    field["data"] = hashed_password
        con = open_db_connection()
        id = insert(con, self)
        profile = Profile()
        field_list = []
        for field in self.fields:
            for profile_field in profile.fields:
                if field["name"] == profile_field["name"]:
                    profile_field["data"] = field["data"]
                if profile_field["name"] == 'user_id':
                    profile_field["data"] = id
        profile.create_profile()
        con.close()


class Login(Model):
    def __init__(self):
        super().__init__()

    fields = [
        Field(
            name='username',
            display_name='Username',
            data_type=str,
            max_length=20,
            data=None,
            visible=True
        ),
        Field(
            name='password',
            display_name='Password',
            data_type=str,
            max_length=32,
            data=None,
            visible=True
        ),
    ]


class Logout(Model):
    def __init__(self):
        super().__init__()

    fields = [
        Field(
            name='username',
            display_name='Username',
            data_type=str,
            max_length=20,
            data='{%print(session.user, end="")%}',
            visible=False
        )
    ]

