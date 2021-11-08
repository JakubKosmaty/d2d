from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlmodel import select
from sqlmodel import Session

from ..models.category import Category
from ..models.category import CategoryCreate
from ..models.category import CategoryRead
from ..models.item import Item
from ..models.item import ItemCreate
from app.database import get_session
from app.helpers import get_category_by_id

router = APIRouter(tags=["Categories"])


@router.get("/categories/", response_model=List[CategoryRead])
def get_categories(*, session: Session = Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories


@router.post("/categories/", response_model=CategoryRead)
def create_category(
    *, session: Session = Depends(get_session), category: CategoryCreate
):
    db_category = Category.from_orm(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


@router.put("/categories/{category_id}/", response_model=CategoryRead)
def edit_category(
    *,
    session: Session = Depends(get_session),
    category_id: int,
    category: CategoryCreate
):
    category_db = get_category_by_id(session, category_id)
    category_db.name = category.name
    session.add(category_db)
    session.commit()
    session.refresh(category_db)
    return category_db


@router.delete("/categories/{category_id}/")
def delete_category(*, session: Session = Depends(get_session), category_id: int):
    category_db = get_category_by_id(session, category_id)
    session.delete(category_db)
    session.commit()
    return status.HTTP_200_OK


@router.get("/categories/{category_id}/items/", response_model=List[Item])
def get_items(*, session: Session = Depends(get_session), category_id: int):
    category = get_category_by_id(session, category_id)
    return category.items


@router.post("/categories/{category_id}/items/", response_model=Item)
def create_item(
    *, session: Session = Depends(get_session), category_id: int, item: ItemCreate
):
    category = get_category_by_id(session, category_id)
    db_item = Item(name=item.name, price=item.price, category_id=category.id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
