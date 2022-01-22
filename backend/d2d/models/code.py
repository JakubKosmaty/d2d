from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel


class CodeBase(SQLModel):
    code: str
    discount: int


class CodeCreate(CodeBase):
    pass


class CodeRead(CodeBase):
    id: int
    used: bool


class Code(CodeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    used: Optional[bool] = Field(default=False)
