from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .item import Item


class CategoryBase(SQLModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    items: List["Item"] = Relationship(back_populates="category")
