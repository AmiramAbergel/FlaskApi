from home_assignment.dal.Message_repository import MessagesRepository

MESSAGES_REPOSITORY = MessagesRepository()


class ReadMessageFlow:
    def __init__(self, id):
        self.id = id

    def get_specific(self):
        return MESSAGES_REPOSITORY.get_specific()
