from typing import Optional
from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: str
    publisher: Optional[bool]
