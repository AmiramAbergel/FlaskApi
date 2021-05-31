from home_assignment.dal.Message_repository import MESSAGES_REPOSITORY


class ReadOneMessageFlow:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_one(self):
        return MESSAGES_REPOSITORY.read_message()
