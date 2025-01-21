from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated

from ..database.db import db_dependency
from ..database.models.users import User
from ..schemas.users import UserBase
from ..services.auth import AuthService

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

user_dependency = Annotated[dict, Depends(AuthService.get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK, response_model=UserBase)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
     
    
    user_model = db.query(User).filter(User.id == user.get('id')).first()
    if user_model is not None:
        return user_model
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User details not found")