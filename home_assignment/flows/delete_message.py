from home_assignment.dal.Message_repository import MessagesRepository

MESSAGES_REPOSITORY = MessagesRepository()


class DeleteMessageFlow:
    def __init__(self, name):
        self.name = name

    def delete_message(self):
        return MESSAGES_REPOSITORY.delete_message()

