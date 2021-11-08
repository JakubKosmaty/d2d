from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class UserBase(SQLModel):
    username: str
    password: str
    email: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
