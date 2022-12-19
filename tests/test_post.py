import requests
from tests.config.config import ENDPOINT, USER_DIR


def test_post_create_user():
    name = "Evgeniy"
    job = "QA Engineer"

    payload = {
        "name": name,
        "job": job,
    }

    response = requests.post(ENDPOINT+USER_DIR, json=payload)
    print(response)

    status = response.status_code
    assert status == 201

    data = response.json()
    print(data)
    assert data["name"] == name
    assert data["job"] == job


