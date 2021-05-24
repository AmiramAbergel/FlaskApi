from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    user_id: int
    name: str
    title: str
    message: str
    read: bool
    created_at: datetime = datetime.now()
