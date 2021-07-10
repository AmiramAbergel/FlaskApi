from messaging_system.dal.Message_repository import MessagesRepository


class UnreadMessageFlow:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def unread_one(self, user_id: int) -> str:
        return MessagesRepository().get_all_user_unread_messages(user_id)