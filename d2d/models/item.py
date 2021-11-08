from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .category import Category
    from .order import OrderItem


class ItemBase(SQLModel):
    name: str
    price: float


class ItemCreate(ItemBase):
    pass


class ItemEdit(ItemBase):
    category_id: int


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional["Category"] = Relationship(back_populates="items")

    order_header_links: List["OrderItem"] = Relationship(back_populates="item")
