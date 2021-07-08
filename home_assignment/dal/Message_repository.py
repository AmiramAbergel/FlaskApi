import secrets

from dal.inmemory_database import In_Memory_Database
from model.config_model import Message
from app import db

class MessagesRepository:
    def __init__(self):
        self.db = db

    def write_message(self, message: Message):
        self.db.session.add(message)

    # Extra
    def get_messages_from_all(self):
        return self.messages_list

    def get_all_user_messages(self, user_id: int) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id, user_messages_list))
        message[0].read = True
        user_id: str = message[0].user_id
        name: str = message[0].name
        title = message[0].title
        user_message = message[0].message
        read = message[0].read
        created_at = message[0].created_at
        return {f"id: {user_id}, "
                f"name: {name}, "
                f"title: {title}, "
                f"message: {user_message}, "
                f"read: {read}, "
                f"created_at: {created_at} "
                }

    def get_all_user_unread_messages(self, user_id: int) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id and m.read == False, user_messages_list))
        return message[0]

    def read_message(self):
        secrets.choice(self.messages_list)

    def delete_message(self, user_id: int) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id, user_messages_list))
        self.messages_list.remove(message[0])
        print(self.messages_list)
        return "Deleted!", 200