# Import the framework
from flask import Flask, request
from home_assignment.flows.delete_message import DeleteMessageFlow
from home_assignment.flows.get_all_unread_user_messages import UnreadMessageFlow
from home_assignment.flows.get_all_user_messages import ReadMessageFlow
from home_assignment.flows.read_one_message import ReadOneMessageFlow
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
        user_id = request_data['id']
        name = request_data['name']
        title = request_data['title']
        message = request_data['message']
        read = False
        created_at = request_data['created_at']

        flow = SendMessageFlow("Test1")
        result = flow.send(user_id, name, title, message, read, created_at)
        return {"New message": f"id: {result.user_id}, "
                               f"name: {result.name}, "
                               f"title: {result.title}, "
                               f"message: {result.message}, "
                               f"read: {result.read}, "
                               f"created_at: {result.created_at} "
                }

    @app2.route('/messages/<int:user_id>', methods=['GET'])
    def get_message(user_id):
        flow = ReadMessageFlow(user_id)
        result = flow.get_specific(user_id)
        return {"Messages": f" {result}"}

    # additional route not in the mission
    @app2.route("/messages", methods=["GET"])
    def get_all_messages():
        flow = SendMessageFlow("stam")
        result = flow.get_all()

        return {"message": f" {result}"}

    @app2.route('/messages/unread/<int:user_id>', methods=['GET'])
    def get_unread_message(user_id):
        flow = UnreadMessageFlow(user_id)
        result = flow.unread_one(user_id)
        return {"unread messages": f" {result}"}

    @app2.route('/messages/random', methods=['GET'])
    def get_one_message():
        flow = ReadOneMessageFlow()
        result = flow.get_one()
        return {"One random messages": f" {result}"}

    @app2.route('/messages/delete/<int:user_id>', methods=['DELETE'])
    def delete_message(user_id):
        flow = DeleteMessageFlow(user_id)
        result = flow.delete_message(user_id)

        return {"Your post has been": f" {result}"}
