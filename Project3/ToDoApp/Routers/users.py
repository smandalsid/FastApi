from fastapi import Depends, HTTPException, status, Path, APIRouter
from models import Users
from database import sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext

router=APIRouter()


router=APIRouter(
    prefix='/users',
    tags=['users'],
)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session, Depends(get_db)]
user_dependency=Annotated[dict, Depends(get_current_user)]
bcrypt_context=CryptContext(schemes=['bcrypt'], deprecated='auto')

class ChangePasswordRequest(BaseModel):
    password: str
    new_password: str

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed!")
    
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()
    if user_model is not None:
        return user_model
    else:
        raise HTTPException(status_code=404, detail="User details not found")
    
@router.put("/change_password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency, db:db_dependency, change_password_reqest: ChangePasswordRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed!")
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()
    if not bcrypt_context.verify(change_password_reqest.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Old password does not match")
    user_model.hashed_password=bcrypt_context.hash(change_password_reqest.new_password)
    db.add(user_model)
    db.commit()

@router.put("/phonenumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user: user_dependency, db: db_dependency, phone_number: str):
    if(user is None):
        raise HTTPException(status_code=401, detail="Authentication Failed!")
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()
    user_model.phone_number=phone_number
    db.add(user_model)
    db.commit()