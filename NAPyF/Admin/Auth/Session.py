from secrets import token_hex


class Session(object):
    def __init__(self):
        self.generate_sid()
    cookie = {}
    user = None
    sid = None
    session = {}

    def generate_sid(self):
        self.sid = token_hex(32)
