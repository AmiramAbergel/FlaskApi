from dal.Message_repository import MessagesRepository


class ReadOneMessageFlow:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def get_one(self):
        return MessagesRepository().read_message()