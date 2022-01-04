import getopt
import sys
import re
from NAPyF.Admin.RequestFunctions import auth_post_user
from pwinput import pwinput
from Settings import TermColors, PASSWORD_REQS, PASSWORD_ERROR_TEXT


def validate_password():
    while True:
        password = pwinput("Enter a password (REQUIRED):\n")
        verify_password = ""
        if not re.match(PASSWORD_REQS, password):
            print(PASSWORD_ERROR_TEXT)
        else:
            verify_password = pwinput("Verify password:\n")
            if password == verify_password:
                break
            print("Passwords do not match. Try again.")
    return password


def validate_username():
    username = ""
    while True:
        if username == "":
            username = input('Type new admin username (REQUIRED):\n')
        else:
            break
    return username


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
                first_name = input('Type new admin first name:\n')
                last_name = input('Type new admin last name:\n')
                email = input('Type new admin email:\n')
                phone_number = input('Type new admin phone number:\n')
                username = validate_username()
                password = validate_password()
                auth_level = 9001
                is_verified = True
                user_attr = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone_number': phone_number,
                    'username': username,
                    'password': password,
                    'auth_level': auth_level,
                    'is_verified': is_verified,
                }
                if auth_post_user(params=user_attr):
                    print(f'Admin {username} created succesfully.')
            except KeyboardInterrupt:
                sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
