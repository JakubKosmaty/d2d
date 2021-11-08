from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import select
from sqlmodel import Session

from app.database import get_session
from app.models.item import Item
from app.models.order import OrderHeader
from app.models.order import OrderHeaderRead
from app.models.order import OrderItem
from app.models.user import User
from app.auth import get_current_user

router = APIRouter(tags=["Orders"])


@router.post("/orders/me/")
def create_order(
    *,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
    items_id: List[int],
):
    order_header = OrderHeader(date=datetime.today(), user_id=user.id)

    for item_id in items_id:
        db_item = session.get(Item, item_id)
        order_link = OrderItem(order_header=order_header, item=db_item, quantity=1)
        session.add(order_link)

    session.commit()

    for link in order_header.item_links:
        print(f"DEBUG: {link.item}")
        print(f"DEBUG: {link.quantity}")


@router.get("/orders/{user_id}/", response_model=List[OrderHeaderRead])
def get_user_orders(*, session: Session = Depends(get_session), user_id: int):
    statement = select(OrderHeader).where(OrderHeader.user_id == user_id)
    orders_list = session.exec(statement).all()
    return orders_list
