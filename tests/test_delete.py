import requests
from tests.config.config import ENDPOINT, USER_DIR


def test_delete_user():
    user_id = "2"

    response = requests.delete(ENDPOINT+USER_DIR+user_id)
    print(response)

    status = response.status_code
    assert status == 204




