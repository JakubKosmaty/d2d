from fastapi import HTTPException
from fastapi import status
from sqlmodel import Session

from .models.category import Category
from .models.item import Item


def get_category_by_id(session: Session, category_id: int) -> Category:
    category: Category = session.get(Category, category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category doesn't exist",
        )
    return category


def get_item_by_id(session: Session, item_id: int) -> Item:
    item: Item = session.get(Item, item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Item doesn't exist",
        )
    return item
