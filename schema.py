from pydantic import BaseModel
from models import GameStatus


class UserBase(BaseModel):
    name: str


class UserDisplay(BaseModel):
    name: str
    status : GameStatus

    class Config:
        from_orm = True


class UserAuth(BaseModel):
    id: int
    name: str


    class Config:
        from_attributes = True