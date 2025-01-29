from fastapi import status
from jose import jwt
from datetime import datetime

from tests.unit.conftest import *

def test_get_user(client, user, test_user: User):
    response = client.get(url="/users/")
    assert response.status_code == status.HTTP_200_OK

    user = response.json()
    assert user["username"] == test_user.username
    assert user["first_name"] == test_user.first_name
    assert user["last_name"] == test_user.last_name
    assert user["email"] == test_user.email
    assert user["phone_number"] == test_user.phone_number