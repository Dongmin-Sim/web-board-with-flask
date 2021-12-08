from .. import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    email = db.Column(db.String(120), nullable=True, unique=True)
    user_id = db.Column(db.String(80), nullable=False, unique=True)
    user_pw = db.Column(db.String(80), nullable=False)
    interesting = db.Column(db.String(20), nullable=False)

    def __init__(self, email, user_id, user_pw, interesting) -> None:
        self.email = email
        self.user_id = user_id
        self.user_pw = user_pw
        self.interesting = interesting
