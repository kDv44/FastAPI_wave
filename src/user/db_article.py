from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from ..exeptions import StoryException
from src.user.models import DbArticle
from .schemas import ArticleBase


def create_article(db: Session, request: ArticleBase):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please.")
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        publisher=request.published,
        user_id=request.creator_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(article_id: int, db: Session):
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id '{article_id}' not found.",
        )
    return article
