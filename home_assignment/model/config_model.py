from datetime import datetime
from database import db


class Message(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, unique=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, title, message, read, created_at):
        self.name = name
        self.title = title
        self.message = message
        self.read = read
        self.created_at = created_at
