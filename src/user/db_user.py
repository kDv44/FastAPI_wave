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


def db_get_user(id: int, db: Session):
    return db.query(DbUser).filter(DbUser.id == id).first()


def db_update_user(id: int, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update(
        {
            DbUser.username: request.username,
            DbUser.password: Hash.bcrypt(request.password),
            DbUser.email: request.email,
        }
    )
    db.commit()
    return "accepted."


def db_delete_user(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "deleted."
