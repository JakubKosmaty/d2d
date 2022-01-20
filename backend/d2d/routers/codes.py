from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import select
from sqlmodel import Session

from d2d.database import get_session
from d2d.models.code import Code
from d2d.models.code import CodeRead
from d2d.models.code import CodeCreate

router = APIRouter(tags=["Codes"])


@router.get("/codes/", response_model=List[CodeRead])
def get_codes(*, session: Session = Depends(get_session)):
    codes = session.exec(select(Code)).all()
    return codes


@router.post("/codes/", response_model=Code)
def create_code(
        *, session: Session = Depends(get_session), code: CodeCreate
):
    selected_code = session.exec(select(Code).where(Code.code == code.code)).first()
    if selected_code is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Code already exist"
        )

    db_code = Code.from_orm(code)
    session.add(db_code)
    session.commit()
    session.refresh(db_code)
    return db_code


@router.post("/codes/{code}", response_model=CodeRead)
def use_code(*, session: Session = Depends(get_session), code: str):
    db_code = session.exec(select(Code).where(Code.code == code)).first()
    if db_code is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Code not found'
        )
    if db_code.used:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Code already used'
        )

    db_code.used = True
    session.add(db_code)
    session.commit()
    session.refresh(db_code)

    return db_code
