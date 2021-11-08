from datetime import datetime
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .order_item_link import OrderItemLink


class OrderBase(SQLModel):
    pass


class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    item_links: List["OrderItemLink"] = Relationship(back_populates="order")


class OrderRead(OrderBase):
    date: datetime
