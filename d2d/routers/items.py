from fastapi import APIRouter, Depends, HTTPException, status

from sqlmodel import Session, select
from typing import List


from d2d.database import get_session
from d2d.helpers import get_category_by_id, get_item_by_id
from d2d.models import CategoryRead, Category, User, CategoryCreate, Item, ItemCreate, ItemEdit
from d2d.routers.auth import get_current_user


router = APIRouter(
    tags=['Items']
)


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
