from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import select
from sqlmodel import Session

from d2d.database import get_session
from d2d.models.category import Category
from d2d.models.category import CategoryCreate
from d2d.models.category import CategoryRead
from d2d.models.category import CategoryUpdate
from d2d.models.item import Item

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


@router.patch("/categories/{category_id}/", response_model=CategoryRead)
def edit_category(
    *,
    session: Session = Depends(get_session),
    category_id: int,
    category: CategoryUpdate
):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)

    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


@router.delete("/categories/{category_id}/")
def delete_category(*, session: Session = Depends(get_session), category_id: int):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    session.delete(db_category)
    session.commit()
    return {"ok": True}


@router.get("/categories/{category_id}/items/", response_model=List[Item])
def get_category_items(*, session: Session = Depends(get_session), category_id: int):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    return db_category.items
