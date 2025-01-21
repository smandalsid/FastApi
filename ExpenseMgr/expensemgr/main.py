from fastapi import FastAPI
from .database.db import engine
from .database.models.users import Base

from .routers import auth, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
async def get_health_check():
    return {"Message": "Application looks healthy"}

app.include_router(auth.router)
app.include_router(users.router)