from secrets import token_hex


class Session(object):
    cookie = {}
    user = None
    sid = None
    session = {}

    def generate_sid(self):
        self.sid = token_hex(32)
