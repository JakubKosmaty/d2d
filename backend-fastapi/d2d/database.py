from sqlmodel import create_engine
from sqlmodel import Session
from sqlmodel import SQLModel

from d2d.settings import settings

sqlite_url = f"sqlite:///{settings.DB_NAME}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=settings.DB_ECHO, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
