from datetime import datetime
from typing import List

from fastapi import APIRouter, Body
from fastapi import Depends
from sqlmodel import select
from sqlmodel import Session

from d2d.database import get_session
from d2d.models.item import Item
from d2d.models.order import Order, OrderCreate
from d2d.models.order import OrderRead
from d2d.models.order_item_link import OrderItemLink
from d2d.models.user import User
from d2d.routers.auth import get_current_user

router = APIRouter(tags=["Orders"])


@router.post("/orders/me/")
def create_order(
    *,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
    address: str = Body(...),
    phone: str = Body(...),
    items: List[OrderCreate],
):
    order = Order(date=datetime.today(), user_id=user.id, address=address, phone=phone)

    for item in items:
        db_item = session.get(Item, item.item_id)
        order_item_link = OrderItemLink(order=order, item=db_item, quantity=item.quantity)
        session.add(order_item_link)

    session.commit()


@router.get("/orders/{user_id}/", response_model=List[OrderRead])
def get_user_orders(*, session: Session = Depends(get_session), user_id: int):
    statement = select(Order).where(Order.user_id == user_id)
    orders_list = session.exec(statement).all()
    return orders_list
