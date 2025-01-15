from fastapi import APIRouter

from ..database.db import db_dependency

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

