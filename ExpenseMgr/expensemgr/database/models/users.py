from ..db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Double

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    is_admin = Column(Boolean, server_default='FALSE')
    last_login = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
