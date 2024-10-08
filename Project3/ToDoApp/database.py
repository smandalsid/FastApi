from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL="sqlite:///./todosapps.db"
# engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

SQLALCHEMY_DATABASE_URL="postgresql://postgres:password@localhost/TodoApplicationDatabase"
engine=create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
