from home_assignment.dal.Message_repository import MessagesRepository

MESSAGES_REPOSITORY = MessagesRepository()


class ReadOneMessageFlow:
    def __init__(self, id):
        self.id = id

    def get_specific_unread(self):
        return MESSAGES_REPOSITORY.read_one()
