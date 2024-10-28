from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

import db_user as db_req

from .schemas import UserBase, UserDisplay
from ..database.db_config import get_db


router = APIRouter(prefix="/user", tags=["user"])


# ===================================================================
# post
# ===================================================================
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_req.db_create_user(db, request)


# ===================================================================
# read
# ===================================================================
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_req.db_get_all_users(db)


@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_req.db_get_user(db, id)
