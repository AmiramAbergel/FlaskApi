from dal.Message_repository import MessagesRepository
from model.config_model import Message


class SendMessageFlow:
    def __init__(self, name: str):
        self.name = name

    def send(self, user_id: int, name: str, title: str, message: str, read: bool, created_at: str) -> str:
        message = Message(user_id, name, title, message, read, created_at)
        MessagesRepository().write_message(message)
        return message

    # all messages all users - not in the mission
    def get_all(self):
        return MessagesRepository().get_messages_from_all()

