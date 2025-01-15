from fastapi import HTTPException, status

from ..database.db import db_dependency
from ..schemas.users import CreateUser, UserBase
from ..database.models.users import User

from .utils import bcrypt_context

class UserService:

    def __init__(self, db: db_dependency):
        self.db = db

    def create_user(self, create_user: CreateUser) -> UserBase:

        if self.db.query(User).filter(User.username == create_user.username).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
        if self.db.query(User).filter(User.phone_number == create_user.phone_number).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Phone number already exists")
        if self.db.query(User).filter(User.email == create_user.email).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        
        # if self.db.query(User).filter
        create_user_model = User(
            email = create_user.email,
            first_name = create_user.first_name,
            last_name = create_user.last_name,
            username = create_user.username,
            password = bcrypt_context.hash(create_user.password),
            phone_number = create_user.phone_number
        )
        self.db.add(create_user_model)
        self.db.commit()

        user = self.db.query(User).filter(User.id == create_user_model.id).first()
        return user
