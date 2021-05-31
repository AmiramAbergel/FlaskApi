import secrets
from typing import List
from home_assignment.model.config_model import Message


class InMemoryDatabase:
    def __init__(self):
        self.messages_list = []

    def add(self, message: Message):
        self.messages_list.append(message)

    # all messages all users - not in the mission
    def get_all(self) -> List[Message]:
        return self.messages_list

    def get_by_id(self, user_id) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id, user_messages_list))
        message[0].read = True
        return message[0]

    def get_specific_unread(self, user_id) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id and m.read == False, user_messages_list))
        return message[0]

    def read_one(self, message: Message):
        secrets.choice(self.messages_list)

    def delete_message(self, user_id) -> str:
        user_messages_list = self.messages_list
        message = list(filter(lambda m: m.user_id == user_id, user_messages_list))
        self.messages_list.remove(message[0])
        print(self.messages_list)
        return "Deleted!", 200