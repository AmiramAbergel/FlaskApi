from home_assignment.dal.Message_repository import Message, MESSAGES_REPOSITORY
from datetime import datetime


class SendMessageFlow:
    def __init__(self, name):
        self.name = name

    def send(self, user_id: int, name: str, title: str, message: str, read: bool, created_at: str) -> str:
        message = Message(user_id, name, title, message, read, created_at)
        MESSAGES_REPOSITORY.write_message(message)
        return message

    # all messages all users - not in the mission
    def get_all(self):
        return MESSAGES_REPOSITORY.get_messages_from_all()



