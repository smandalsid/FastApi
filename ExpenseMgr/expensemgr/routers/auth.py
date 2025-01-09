from fastapi import APIRouter, status


from ..database.db import db_dependency
from ..schemas.users import CreateUser, UserBase

from ..services.users import *

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserBase)
async def create_user(db: db_dependency, create_user: CreateUser):
    service = UserService(db=db)
    return service.create_user(create_user=create_user)
    
