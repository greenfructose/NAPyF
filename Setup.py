import getopt
import sys
import re
from NAPyF.Admin.RequestFunctions import auth_post_user
from pwinput import pwinput
from Settings import TermColors, PASSWORD_REQS, PASSWORD_ERROR_TEXT, USERNAME_REQS, USERNAME_ERROR_TEXT, NAME_REQS, \
    NAME_ERROR_TEXT, EMAIL_REQS, EMAIL_ERROR_TEXT


def validate_password(password):
    while True:
        verify_password = ""
        if not re.match(PASSWORD_REQS, password):
            print(PASSWORD_ERROR_TEXT)
        else:
            verify_password = pwinput("Verify password:\n")
            if password == verify_password:
                break
            print("Passwords do not match. Try again.")
    return password


def validate_username(username):
    while True:
        if not re.match(USERNAME_REQS, username):
            print(USERNAME_ERROR_TEXT)
        else:
            break
    return username


validation_dict = {
    0: ('Type new admin first name:\n', 'first_name', NAME_REQS, NAME_ERROR_TEXT),
    1: ('Type new admin last name:\n', 'last_name', NAME_REQS, NAME_ERROR_TEXT),
    2: ('Type new admin email:\n', 'email', EMAIL_REQS, EMAIL_ERROR_TEXT),
    3: ('Enter a username (REQUIRED):\n', 'username', USERNAME_REQS, USERNAME_ERROR_TEXT),
    4: ('Enter a password (REQUIRED):\n', 'password', PASSWORD_REQS, PASSWORD_ERROR_TEXT),
}


def validate(case, prompt, label, reqs, error):
    while True:
        if case != 4:
            test = input(prompt)
        else:
            test = pwinput(prompt)
        if not re.match(reqs, test):
            print(error)
        else:
            if case == 4:
                verify_password = pwinput("Verify password:\n")
                if test == verify_password:
                    break
            else:
                break
    return {label: test}


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "", ["createadmin"])
    except getopt.GetoptError:
        print('Some error occured')
        print('Setup.py -createadmin             ----- Create Admin User')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--createadmin":
            try:
                user_attr = {}
                for key, value in validation_dict.items():
                    user_attr = user_attr | validate(key, value[0], value[1], value[2], value[3])
                user_attr = user_attr | {'auth_level': 9001, 'is_verified': True}
                if auth_post_user(params=user_attr) is not None:
                    print(f'Admin {user_attr["username"]} created succesfully.')
            except KeyboardInterrupt:
                sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
