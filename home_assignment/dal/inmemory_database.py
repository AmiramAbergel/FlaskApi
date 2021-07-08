import secrets
import pprint
from typing import List
from model.config_model import Message


class InMemoryDatabase:
    def __init__(self):
        self.messages_list = []

    def add(self, message: Message):
        self.messages_list.append(message)

    # all messages all users - not in the mission
    def get_all(self) -> List[Message]:
        return self.messages_list

    def get_by_id(self, user_id: int) -> str:
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


    def get_specific_unread(self, user_id: int) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id and m.read == False, user_messages_list))
        return message[0]

    def read_one(self, message: Message):
        secrets.choice(self.messages_list)

    def delete_message(self, user_id: int) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id, user_messages_list))
        self.messages_list.remove(message[0])
        print(self.messages_list)
        return "Deleted!", 200


In_Memory_Database = InMemoryDatabase()