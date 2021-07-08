# Import the framework
from flask import Flask, request, json
from flows.delete_message import DeleteMessageFlow
from flows.get_all_unread_user_messages import UnreadMessageFlow
from flows.get_all_user_messages import ReadMessageFlow
from flows.read_one_message import ReadOneMessageFlow
from flows.send_message import SendMessageFlow
from model.config_model import Message


def messages_router(app):

    @app.route('/messages/write', methods=['POST'])
    def send_message() -> str:
        request_data = request.get_data()
        data = json.loads(request_data)
        name = data.get('name')
        title = data.get('title')
        message = data.get('message')
        read = False
        created_at = data.get('created_at')

        res_message = Message(name, title, message, read, created_at)
        flow = SendMessageFlow(res_message)
        result = flow.send()
        return {"New message": f"id: {result.user_id}, "
                               f"name: {result.name}, "
                               f"title: {result.title}, "
                               f"message: {result.message}, "
                               f"read: {result.read}, "
                               f"created_at: {result.created_at} "
                }

    @app.route('/messages/<int:user_id>', methods=['GET'])
    def get_message(user_id: int) -> str:
        flow = ReadMessageFlow(user_id)
        result = flow.get_specific(user_id)
        return {"User - " f"{user_id}" " Messages": f"{result}"}

    # additional route not in the mission
    @app.route("/messages", methods=["GET"])
    def get_all_messages() -> str:
        flow = SendMessageFlow("stam")
        result = flow.get_all()

        return {"message": f" {result}"}

    @app.route('/messages/unread/<int:user_id>', methods=['GET'])
    def get_unread_message(user_id: int) -> str:
        flow = UnreadMessageFlow(user_id)
        result = flow.unread_one(user_id)
        return {"unread messages": f" {result}"}

    @app.route('/messages/random', methods=['GET'])
    def get_one_message() -> str:
        flow = ReadOneMessageFlow()
        result = flow.get_one()
        return {"One random messages": f" {result}"}

    @app.route('/messages/delete/<int:user_id>', methods=['DELETE'])
    def delete_message(user_id: int) -> str:
        flow = DeleteMessageFlow(user_id)
        result = flow.delete_message(user_id)

        return {"Your post has been": f" {result}"}
