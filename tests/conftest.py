import pytest
from app import create_app
from shutil import copy
import constants
import os


@pytest.fixture
def client(tmpdir):
    copy(constants.REFERENCE_TEST_DATABASE_PATH, tmpdir.dirpath())
    temp_db_path = os.path.join(tmpdir.dirpath(), constants.REFERENCE_DB_NAME)
    app = create_app(db_path=temp_db_path)
    with app.test_client() as client:
        yield client
