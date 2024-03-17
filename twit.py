from user import User


class Twit:

    def __init__(self, body: str, author: User, id=None):
        self.body = body
        self.author = author
        self.id = id


    def to_dict(self):
        return {'id': self.id, 'body': self.body, 'author': self.author}