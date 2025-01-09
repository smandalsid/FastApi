from ..database.db import db_dependency
from ..schemas.users import CreateUser, UserBase
from ..database.models.users import User

class UserService:

    def __init__(self, db: db_dependency):
        self.db = db

    def create_user(self, create_user: CreateUser) -> UserBase:
        create_user_model = User(**create_user.model_dump())
        self.db.add(create_user_model)
        self.db.commit()

        user = self.db.query(User).filter(User.id == create_user_model.id).first()
        return user
