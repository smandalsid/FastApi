from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from ..database import Base

from ..main import app
from ..Routers.todos import get_db, get_current_user

from fastapi.testclient import TestClient
from fastapi import status
import pytest
from ..models import Todos, Users
from ..Routers.auth import bcrypt_context

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/TestDB"
# engine=create_engine(
#     SQLALCHEMY_DATABASE_URL,
# )




SQLALCHEMY_DATABASE_URL ="sqlite:///./testdb.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass = StaticPool,
)

TestingSessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username':'testuser', 'id':1, 'user_role':'admin'}

app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user

client=TestClient(app)

@pytest.fixture
def test_todo():
    todo=Todos(
        title="title",
        description="description",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db=TestingSessionLocal()


    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user=Users(
        username='username',
        email='email',
        first_name='fname',
        last_name='lname',
        hashed_password=bcrypt_context.hash('password'),
        role='admin',
        phone_number='123',
    )

    db=TestingSessionLocal()
    db.add(user)
    db.commit()

    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM USERS;"))
        connection.commit()