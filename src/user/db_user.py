from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from src.user.models import DbUser
from ..database.hash import Hash
from .schemas import UserBase


def db_create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def db_get_all_users(db: Session):
    return db.query(DbUser).all()


def db_get_user(user_id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found.",
        )
    return user


def db_update_user(user_id: int, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found.",
        )
    user.update(
        {
            DbUser.username: request.username,
            DbUser.password: Hash.bcrypt(request.password),
            DbUser.email: request.email,
        }
    )
    db.commit()
    return "accepted."


def db_delete_user(user_id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found.",
        )
    db.delete(user)
    db.commit()
    return "deleted."
