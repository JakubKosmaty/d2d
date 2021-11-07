from fastapi import HTTPException, status

from sqlmodel import Session

from d2d.models import Category, Item


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
