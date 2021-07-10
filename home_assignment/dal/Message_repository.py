import secrets
from database import db
from model.config_model import Message


class MessagesRepository:
    def __init__(self):
        self.db = db

    def write_message(self, message: Message):
        self.db.session.add(message)
        self.db.session.commit()
        return message

    # Extra
    def get_messages_from_all(self):
        messages = Message.query.all()
        return messages

    def get_all_user_messages(self, user_id: int) -> str:
        message = Message.query.filter_by(user_id=user_id).first_or_404()
        message.read = True
        user_id = message.user_id
        name = message.name
        title = message.title
        user_message = message.message_content
        read = message.read
        created_at = message.created_at
        return {f"id: {user_id}, "
                f"name: {name}, "
                f"title: {title}, "
                f"message: {user_message}, "
                f"read: {read}, "
                f"created_at: {created_at} "
                }

    def get_all_user_unread_messages(self, user_id: int) -> str:
        message = Message.query.filter_by(user_id=user_id).filter_by(read=False)
        return message

    def read_message(self):
        secrets.choice(self.messages_list)

    def delete_message(self, user_id: int) -> str:
        message = Message.query.filter_by(user_id=user_id).first_or_404()
        self.db.session.delete(message)
        return "Deleted!", 200