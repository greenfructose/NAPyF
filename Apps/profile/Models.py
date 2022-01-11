from NAPyF.DataBase import open_db_connection, insert
from NAPyF.Model import Model
from NAPyF.Types import Field, ForeignKey
from datetime import datetime

class Profile(Model):
    def __init__(self):
        super().__init__()

    name = 'profile'
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
            name='picture',
            display_name='Profile Picture',
            data_type=str,
            max_length=100,
            data=None,
            visible=True
        ),
        Field(
            name='user_id',
            display_name='User ID',
            data_type=int,
            max_length=100,
            data=None,
            visible=True,
            foreign_key=ForeignKey('user_id', 'user', 'user_id').get_key_string()
        )
    ]

    def create_profile(self):
        username = ''
        for field in self.fields:
            if field["name"] == 'username':
                username = field["data"]
            if field["name"] == 'picture':
                field["data"] = f'/{username}'
        con = open_db_connection()
        insert(con, self)
        con.close()



