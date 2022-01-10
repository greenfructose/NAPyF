from NAPyF.DataBase import open_db_connection, insert
from NAPyF.Model import Model
from NAPyF.Types import Field
from Settings import APPS_DIR, BASE_DIR

import os


class Profile(Model):
    def __init__(self):
        super().__init__()

    name = 'profiles'
    fields = [
        Field(
            name='profiles_id',
            display_name='Profile ID',
            data_type=int,
            max_length=20,
            data=None,
            visible=False
        ),
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
            name='picture',
            display_name='Profile Picture',
            data_type=str,
            max_length=100,
            data=None,
            visible=True
        ),
    ]

    def create_profile(self, **kwargs):
        for key, value in kwargs.items():
            for field in self.fields:
                if field["name"] == key:
                    field["data"] = kwargs[key]
                if field["name"] == 'picture':
                    field["data"] = APPS_DIR + '/profile/base/profiles/default_profile_picture.png'
        con = open_db_connection()
        insert(con, self)
        con.close()



