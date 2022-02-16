import pytest
from app import create_app

#todo: create a test db before and remove the test db after tests

@pytest.fixture
def client():
    print("fixture")
    app = create_app()
    with app.test_client() as client:
        yield client
