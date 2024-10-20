from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from .db_user import create_user as db_create_user
from .schemas import UserBase, UserDisplay
from ..database.db_config import get_db


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_create_user(db, request)
