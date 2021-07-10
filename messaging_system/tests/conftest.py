import pytest
from messaging_system import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    testing_client = flask_app.test_client()

    return testing_client