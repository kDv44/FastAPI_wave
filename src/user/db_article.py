from sqlalchemy.orm.session import Session

from src.user.models import DbArticle
from .schemas import ArticleBase


def create_article(db: Session, request: ArticleBase):
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
    return article
