from sqlalchemy.orm.session import Session

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


def db_get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()
