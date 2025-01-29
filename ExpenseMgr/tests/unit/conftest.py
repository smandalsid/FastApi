import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from typing import Generator
import os
from datetime import timedelta
from jose import jwt

from expensemgr.database.db import Base, get_db
from expensemgr.main import app
from expensemgr.services.auth import AuthService
from expensemgr.services.utils import bcrypt_context
from expensemgr.database.models.users import User
from expensemgr.services.utils import *

load_dotenv()

SQLITE_DATABASE_URL = os.getenv("TESTDB_URL")

engine = create_engine(SQLITE_DATABASE_URL)

TestingSessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_test_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db(setup_test_database):
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind = connection)
    
    yield session
    session.close()
    transaction.rollback()
    connection.close()

# def override_get_db(db):
#         try:
#             yield db
#         finally:
#             db.close()
# def override_get_current_user():
#     return {'username':'testuser', 'id':1, 'is_admin':False}

# app.dependency_overrides[AuthService.get_current_user]=override_get_current_user
# app.dependency_overrides[get_db]=override_get_db

# client = TestClient(app)

@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient, any, any]:
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db]=override_get_db

    def override_get_current_user():
        return {'username':'testuser', 'id':1, 'is_admin':False}
    app.dependency_overrides[AuthService(db).get_current_user]=override_get_current_user

    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def test_user(db):
    user = User(
        username='testuser',
        phone_number='1111111111',
        email='test@mail.com',
        first_name='firstname',
        last_name='lastname',
        password=bcrypt_context.hash('password'),
    )
    db.add(user)
    db.commit()

    yield user

    # with engine.connect() as connection:
    #     connection.execute(text("DELETE FROM USERS;"))
    #     connection.commit()


# @pytest.fixture(autouse=True)
# def set_session_for_factories(db: Session):
#     UserFactory._meta.sqlalchemy_session = db


@pytest.fixture(scope="function")
def user(db, test_user, client: TestClient):
    user : User = test_user
    access_token: str = AuthService(db).create_access_token(user.username, user.id, user.is_admin, timedelta(30))
    headers = {'Authorization' : f"Bearer {access_token}"}
    client.headers.update(headers)
    yield user
    client.headers.clear()