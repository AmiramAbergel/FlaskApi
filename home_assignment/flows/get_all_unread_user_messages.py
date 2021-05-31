from home_assignment.dal.Message_repository import MESSAGES_REPOSITORY


class UnreadMessageFlow:
    def __init__(self, user_id):
        self.user_id = user_id

    def unread_one(self, user_id):
        return MESSAGES_REPOSITORY.get_all_user_unread_messages(user_id)
