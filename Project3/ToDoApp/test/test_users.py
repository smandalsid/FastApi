from .utils import *
from ..Routers.users import get_current_user, get_db

app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user

def test_return_user(test_user):
    response=client.get("/users/")
    assert response.status_code==status.HTTP_200_OK
    assert response.json()['username']=='username'
    assert response.json()['email']=='email'
    assert response.json()['first_name']=='fname'
    assert response.json()['last_name']=='lname'
    assert response.json()['role']=='admin'
    assert response.json()['phone_number']=='123'

def test_change_password_success(test_user):
    response=client.put("/users/change_password", json={'password':'password', 'new_password':'new_password'})
    assert response.status_code==status.HTTP_204_NO_CONTENT

def test_change_phone_number_success(test_user):
    response=client.put('/users/phonenumber/222222')
    assert response.status_code==status.HTTP_204_NO_CONTENT

