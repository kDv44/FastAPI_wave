from typing import Optional, List
from pydantic import BaseModel


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: str
    publisher: Optional[bool]
    tags: List[str] = []
    image: Optional[Image] = None
