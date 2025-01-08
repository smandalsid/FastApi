from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str


class UserLogin(BaseModel):
    username: str
    password: str
    retyped_password: str


