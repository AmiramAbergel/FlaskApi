from datetime import datetime
from database import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    messages = db.relationship('Message', backref='author', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    message_content = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, unique=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, title, message_content, read, created_at):
        self.title = title
        self.message = message_content
        self.read = read
        self.created_at = created_at
