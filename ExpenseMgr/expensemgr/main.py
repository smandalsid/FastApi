from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database.db import *
from .database.models import users

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

users.Base.metadata.create_all(bind = engine)

app = FastAPI()


@app.get("/health")
async def get_health_check():
    return {"Message": "Application looks healthy"}