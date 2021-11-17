from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import Session

from d2d.database import get_session
from d2d.models.category import Category
from d2d.models.item import Item
from d2d.models.item import ItemCreate
from d2d.models.item import ItemUpdate

router = APIRouter(tags=["Items"])


@router.post("/items/", response_model=Item)
def create_item(*, session: Session = Depends(get_session), item: ItemCreate):
    db_category = session.get(Category, item.category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.patch("/items/{item_id}/", response_model=Item)
def update_item(
    *, session: Session = Depends(get_session), item_id: int, item: ItemUpdate
):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    item_data = item.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(db_item, key, value)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/items/{item_id}/")
def delete_item(*, session: Session = Depends(get_session), item_id: int):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    session.delete(db_item)
    session.commit()
    return {"ok": True}
