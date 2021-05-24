from home_assignment.dal.Message_repository import MessagesRepository

MESSAGES_REPOSITORY = MessagesRepository()


class UnreadMessageFlow:
    def __init__(self, id):
        self.id = id

    def unread_one(self):
        return MESSAGES_REPOSITORY.read_one()
