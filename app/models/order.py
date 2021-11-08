from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .item import Item


class OrderItemBase(SQLModel):
    pass


class OrderItem(OrderItemBase, table=True):
    order_id: Optional[int] = Field(
        default=None, foreign_key="orderheader.id", primary_key=True
    )
    item_id: Optional[int] = Field(
        default=None, foreign_key="item.id", primary_key=True
    )

    quantity: int

    order_header: "OrderHeader" = Relationship(back_populates="item_links")
    item: "Item" = Relationship(back_populates="order_header_links")


class OrderHeaderBase(SQLModel):
    pass


class OrderHeader(OrderHeaderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    item_links: List[OrderItem] = Relationship(back_populates="order_header")


class OrderHeaderRead(OrderHeaderBase):
    item_links: List[OrderItem]
