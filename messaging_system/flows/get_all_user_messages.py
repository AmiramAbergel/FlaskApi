from messaging_system.dal.Message_repository import MessagesRepository
from messaging_system.model.config_model import Message

class ReadMessageFlow:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def read_specific(self, user_id: int, name: str, title: str, message: str, read: bool) -> str:
        message = Message(user_id, name, title, message, read)
        MessagesRepository().write_message(message)
        return message

    def get_specific(self, user_id: int) -> str:
        return MessagesRepository().get_all_user_messages(user_id)

