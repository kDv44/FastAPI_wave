from sqlalchemy.orm.session import Session

from .schemas import UserBase
from src.user.models import DbUser
from ..database.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
