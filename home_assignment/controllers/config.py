from flask import json

json_file_path = 'controllers/data.json'
with open(json_file_path, 'r') as text_file_input:
    data = text_file_input.read()
# loading that file as a JSON object
obj = json.loads(data)
