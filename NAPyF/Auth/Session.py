from random import randint


class Session(object):
    cookie = {}
    user = None
    sid = None
    session = {}

    def generate_sid(self):
        self.sid = "".join(str(randint(1, 9)) for _ in range(100))


