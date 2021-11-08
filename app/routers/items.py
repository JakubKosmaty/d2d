from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlmodel import Session

from ..models.item import Item
from ..models.item import ItemEdit
from app.database import get_session
from app.helpers import get_category_by_id
from app.helpers import get_item_by_id

router = APIRouter(tags=["Items"])


@router.put("/items/{item_id}/", response_model=Item)
def edit_item(*, session: Session = Depends(get_session), item_id: int, item: ItemEdit):
    item_db = get_item_by_id(session, item_id)
    item_db.name = item.name
    item_db.price = item.price

    category = get_category_by_id(session, item.category_id)
    item_db.category = category

    session.add(item_db)
    session.commit()
    session.refresh(item_db)
    return item_db


@router.delete("/items/{item_id}/")
def delete_item(*, session: Session = Depends(get_session), item_id: int):
    item_db = get_item_by_id(session, item_id)
    session.delete(item_db)
    session.commit()
    return status.HTTP_200_OK
