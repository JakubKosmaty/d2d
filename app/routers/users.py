from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from ..database import get_session
from ..models.user import User
from ..models.user import UserCreate
from ..models.user import UserRead
from .auth import get_password_hash


router = APIRouter(tags=["Users"])


@router.post("/users/", response_model=UserRead)
def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    user.password = get_password_hash(user.password)
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
