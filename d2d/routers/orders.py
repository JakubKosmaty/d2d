from datetime import date
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import select
from sqlmodel import Session

from ..models.item import Item
from ..models.order import OrderHeader
from ..models.order import OrderItem
from ..models.user import User
from d2d.database import get_session
from d2d.routers.auth import get_current_user


router = APIRouter(tags=["Orders"])


@router.post("/orders/")
def create_order(
    *,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
    items_id: List[int],
):
    order_header = OrderHeader(
        date=datetime.today().strftime("%Y-%m-%d-%H:%M:%S"), user_id=user.id
    )

    for id in items_id:
        db_item = session.get(Item, id)
        order_link = OrderItem(order_header=order_header, item=db_item, quantity=1)
        session.add(order_link)

    session.commit()

    for link in order_header.item_links:
        print(f"DEBUG: {link.item}")
        print(f"DEBUG: {link.quantity}")
