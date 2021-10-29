from db_connect import db
from datetime import date, datetime


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    author = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, author, content) -> None:
        self.author = author
        self.content = content


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    email = db.Column(db.String(120), nullable=True, unique=True)
    user_id = db.Column(db.String(80), nullable=False, unique=True)
    user_pw = db.Column(db.String(80), nullable=False)

    def __init__(self, email, user_id, user_pw) -> None:
        self.email = email
        self.user_id = user_id
        self.user_pw = user_pw
