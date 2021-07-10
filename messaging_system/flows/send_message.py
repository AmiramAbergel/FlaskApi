from messaging_system.dal.Message_repository import MessagesRepository
from messaging_system.model.config_model import Message


class SendMessageFlow:
    def __init__(self, message: Message):
        self.message_repository = MessagesRepository()
        self.new_message = message

    def send(self) -> str:
        message = self.message_repository.write_message(self.new_message)
        return message

    # all messages all users - not in the mission
    def get_all(self):
        return MessagesRepository().get_messages_from_all()

