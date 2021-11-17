from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session, select

from d2d.database import get_session
from d2d.models.order import Order, OrderRead
from d2d.models.user import User
from d2d.models.user import UserCreate
from d2d.models.user import UserRead
from d2d.routers.auth import get_password_hash, get_current_user

router = APIRouter(tags=["Users"])


@router.post("/users/", response_model=UserRead)
def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    user.password = get_password_hash(user.password)
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/users/me", response_model=UserRead)
def get_user(
        *,
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)):
    return user


@router.get("/users/me/orders", response_model=List[OrderRead])
def get_current_user_orders(
        *,
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)):

    statement = select(Order).where(Order.user_id == user.id)
    orders_list = session.exec(statement).all()

    return orders_list
