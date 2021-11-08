import jwt
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from pydantic import parse_obj_as
from sqlmodel import select
from sqlmodel import Session

from d2d.database import get_session
from d2d.models.user import User
from d2d.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(tags=["Auth"])


class Token(BaseModel):
    access_token: str
    token_type: str


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user: User = parse_obj_as(User, payload)
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    return user


def authenticate_user(session: Session, username: str, password: str):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def create_access_token(user: User) -> Token:
    token = jwt.encode(
        user.dict(), settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    token_type = "bearer"
    return Token(access_token=token, token_type=token_type)


@router.post("/token", response_model=Token)
async def generate_token(
    *,
    session: Session = Depends(get_session),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_access_token(user)
