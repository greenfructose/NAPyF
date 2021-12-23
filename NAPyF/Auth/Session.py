from random import randint
from NAPyF.Auth.Models import verify_password

sessions = {}


class Session(object):
    cookie = None
    user = None

    def generate_sid(self):
        return "".join(str(randint(1, 9)) for _ in range(100))

    def login(self, username, password):
        logged_in = False
        if verify_password(username, password):
            sid = self.generate_sid()
            self.cookie = f'sid={sid}'
            sessions[sid] = {"username", "useragent", "ip address", "expiry"}
            logged_in = True
        return logged_in

    def logout(self):
        logged_out = False
        if self.user:
            self.cookie = "sid="
            del sessions[self.user]
            logged_out = True
        return logged_out
