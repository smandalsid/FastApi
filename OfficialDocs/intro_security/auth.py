from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return User(
        username = token + "fakedecoded",
        email = "test@mail.com",
        full_name = "Test Man"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user