from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .item import Item
    from .order import Order


class OrderItemLinkBase(SQLModel):
    pass


class OrderItemLink(OrderItemLinkBase, table=True):
    order_id: Optional[int] = Field(
        default=None, foreign_key="order.id", primary_key=True
    )
    item_id: Optional[int] = Field(
        default=None, foreign_key="item.id", primary_key=True
    )

    quantity: int

    order: "Order" = Relationship(back_populates="item_links")
    item: "Item" = Relationship(back_populates="order_links")
