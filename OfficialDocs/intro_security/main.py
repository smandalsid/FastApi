from typing import Annotated

from fastapi import FastAPI, Depends

from models import User
from auth import get_current_user

app = FastAPI()



@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user