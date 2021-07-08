from dal.inmemory_database import InMemoryDatabase, In_Memory_Database
from model.config_model import Message


class MessagesRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def write_message(self, message: Message):
        self.db.add(message)

    # Extra
    def get_messages_from_all(self):
        self.db.get_all()

    def get_all_user_messages(self, user_id: int) -> str:
        return self.db.get_by_id(user_id)

    def get_all_user_unread_messages(self, user_id: int) -> str:
        return self.db.get_specific_unread(user_id)

    def read_message(self):
        self.db.read_one()

    def delete_message(self, user_id: int) -> str:
        return self.db.delete_message(user_id)