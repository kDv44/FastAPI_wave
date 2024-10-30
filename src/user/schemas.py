from typing import List
from pydantic import BaseModel


# ===================================================
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


# ==================================================


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config:
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: UserBase

    class Config:
        from_attributes = True
