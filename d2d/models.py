from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class UserBase(SQLModel):
    username: str
    password: str
    email: str


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class CategoryBase(SQLModel):
    name: str


class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="category")


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


class ItemBase(SQLModel):
    name: str
    price: float


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="items")


class ItemCreate(ItemBase):
    pass


class ItemEdit(ItemBase):
    category_id: int
