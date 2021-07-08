from dataclasses import dataclass
from datetime import datetime

from app import db


@dataclass
class Message(db.Model):
    user_id: db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    read: db.Column(db.Boolean, unique=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
