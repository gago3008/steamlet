from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    usename: str
    password: str


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    usename: str
    password: str

class ListUser():
    skip: int
    limit: int
    username: str

class DeleteUser():
    username: str

class UserPermissionCreate():
    userId : int
    permissionId : int

class TourCreate():
    tourId: int
    tourName: str
    description: str

class TourUpdate():
    tourName: str
    description: str
    removetime: DateTime