from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .category import Category
    from .order_item_link import OrderItemLink


class ItemBase(SQLModel):
    name: str
    price: float
    image_url: str


class ItemCreate(ItemBase):
    category_id: int


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    image_url: Optional[str] = None


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional["Category"] = Relationship(back_populates="items")

    order_links: List["OrderItemLink"] = Relationship(back_populates="item")
