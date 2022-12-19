import requests
from tests.config.config import ENDPOINT, USER_DIR


def test_get_user():
    user_id = "2"
    user_email = "janet.weaver@reqres.in"

    response = requests.get(ENDPOINT+USER_DIR+user_id)
    print(response)

    status = response.status_code
    assert status == 200

    data = response.json()
    print(data)
    assert data["data"]["email"] == user_email

