""" Models"""

# pylint: disable=too-few-public-methods
class Msg(object):
    """ A Msg to send upon action"""

    def __init__(self, time: int, msgType: str, user_id: str):
        self.time = time
        self.type = msgType
        self.user_id = user_id