import requests
from tests.config.config import ENDPOINT, USER_DIR


def test_put_update_user():
    user_id = "2"
    name = "Evgeniy"
    job = "QA Engineer"

    payload = {
        "name": name,
        "job": job,
    }

    response = requests.put(ENDPOINT+USER_DIR+user_id, json=payload)
    print(response)

    status = response.status_code
    assert status == 200

    data = response.json()
    print(data)
    assert data["name"] == name
    assert data["job"] == job


