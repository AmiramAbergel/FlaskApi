'''''
from flask import json

json_file_path = 'controllers/data.json'


def my_data():
    with open(json_file_path, 'r') as text_file_input:
        data = text_file_input.read()
    # loading that file as a JSON object
    list_of_messages = json.loads(data)
    return list_of_messages


'''''
