import secrets
from flask import jsonify
from typing import List
from home_assignment.app import data_base
from home_assignment.model.config_model import Message


class InMemoryDatabase:
    def __init__(self):
        return


class MessagesRepository:
    def __init__(self):
        self.messages_list = []
        self.messages_list.extend(data_base)

    def add(self, message: Message):
        self.messages_list.append(message)

    # all messages all users - not in the mission
    def get_all(self) -> List[Message]:
        return self.messages_list

    def get_specific(self) -> str:
        message = list(filter(lambda m: m["id"] == id, self.messages_list))
        message[0]['read'] = True
        return jsonify({'messages': message[0]})

    def get_specific_unread(self):
        return

    def read_one(self, message: Message):
        secrets.choice(self.messages_list)

    def delete_message(self):
        return




