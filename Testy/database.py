from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL="postgresql://postgres:password@localhost/TodoApplicationDatabase"
engine=create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()