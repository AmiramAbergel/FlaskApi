from home_assignment.dal.Message_repository import MESSAGES_REPOSITORY


class DeleteMessageFlow:
    def __init__(self, user_id):
        self.user_id = user_id

    def delete_message(self, user_id):
        return MESSAGES_REPOSITORY.delete_message(user_id)

