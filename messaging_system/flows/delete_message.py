from messaging_system.dal.Message_repository import MessagesRepository


class DeleteMessageFlow:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def delete_message(self, user_id: int) -> str:
        return MessagesRepository().delete_message(user_id)