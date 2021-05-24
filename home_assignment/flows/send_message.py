from home_assignment.dal.Message_repository import Message, MessagesRepository

MESSAGES_REPOSITORY = MessagesRepository()


class SendMessageFlow:
    def __init__(self, name):
        self.name = name

    def send(self, user_id: int, name: str, title: str, message: str, read: bool) -> str:
        message = Message(user_id, name, title, message, read)
        MESSAGES_REPOSITORY.add(message)
        return message

    #all messages all users - not in the mission
    def get_all(self):
        return MESSAGES_REPOSITORY.get_all()



