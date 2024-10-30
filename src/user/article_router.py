from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

import src.user.db_article as db_req

from src.user.schemas import ArticleDisplay, ArticleBase
from ..database.db_config import get_db

router = APIRouter(prefix="/article", tags=["article"])


# ===================================================================
# post
# ===================================================================
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_req.create_article(db, request)


# ===================================================================
# read
# ===================================================================
@router.get("/{article_id}", response_model=ArticleDisplay)
def get_article(article_id: int, db: Session = Depends(get_db)):
    return db_req.get_article(article_id, db)
