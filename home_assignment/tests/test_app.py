import pytest
from flask import Flask, json

from controllers.hello_route import router2
from controllers.messages_routes import router

'''
def test_index_page():
    app = Flask(__name__)
    router2(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200
'''


def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data


def test_post_route__success(test_client):
    mock_request_data = {
        "id": 100,
        "name": "Tester",
        "title": "VP-test",
        "message": "Testing user id == 100 message",
        "read": True,
        "created_at": ""
    }
    url = '/messages/write'

    response = test_client.post(url, data=json.dumps(mock_request_data))
    assert response.status_code == 200
