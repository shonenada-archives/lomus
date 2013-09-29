from szufm.app import db


class Demo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)

    def __init__(name):
        self.name = name
