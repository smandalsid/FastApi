from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

from ..database.models.users import User
from ..database.db import db_dependency
from ..schemas.users import CreateUser

load_dotenv()



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["brcypt"], deprecated='auto')
oath2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
