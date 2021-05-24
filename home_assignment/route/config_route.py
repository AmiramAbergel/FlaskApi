from flask import request, jsonify

from home_assignment.controllers.config import obj
from home_assignment.dal import Message_repository
from home_assignment.dal.Message_repository import Message, MessagesRepository
from home_assignment.flows.delete_message import DeleteMessageFlow
from home_assignment.flows.get_all_user_messages import ReadMessageFlow
from home_assignment.flows.send_message import SendMessageFlow


def router(app2):
    # @app.route("/example", methods=["GET"])
    # def example():
    #     return json_dumps({"This Is": "An example"})
    #
    # @app.route("/do", methods=["POST"])
    # def process_application():
    #     request_data = json_loads(request.get_json())
    #     my_param_key = request_data["my_param_key"]
    #     return json_dumps({"message": f"Done with {my_param_key}"})

    @app2.route('/')
    def hello_world():
        return 'Hello World!'

    @app2.route('/messages/write', methods=['POST'])
    def send_message():
        request_data = request.json
        # Get the id of the last user message and create the new one
        user_id = obj[-1]['id'] + 1
        name = request_data['name']
        title = request_data['title']
        message = request_data['message']
        read = False

        flow = SendMessageFlow("Test1")
        result = flow.send(user_id, name, title, message, read)
        return {"New message": f"id: {result.user_id}, "
                               f"name: {result.name}, "
                               f"title: {result.title}, "
                               f"message: {result.message}, "
                               f"read: {result.read} "
                }

    @app2.route('/messages/<int:id>', methods=['GET'])
    def get_message(id):
        flow = ReadMessageFlow(id)
        result = flow.get_specific()
        return {"message": f"number of messages {result}"}

    # additional route not in the mission
    @app2.route("/messages", methods=["GET"])
    def get_messages():
        flow = SendMessageFlow("stam")
        result = flow.get_all()

        return {"message": f" {result}"}

    @app2.route('/messages/unread/<int:id>', methods=['GET'])
    def get_unread_message():

        flow = SendMessageFlow("Test1")
        result = flow.get_all()
        return {"message": f"number of messages {len(result)}"}

    @app2.route('/messages/delete', methods=['DELETE'])
    def delete_message():

        messages = MessagesRepository
        message = filter(lambda m: m['id'] == id, messages)

        flow = DeleteMessageFlow("Test1")
        result = flow.delete()

        return {"One message": f"{result} "}
