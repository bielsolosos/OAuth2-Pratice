from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.user_service import (
    get_user_service,
    create_user_service,
    delete_user_service,
)
from app.repositories.user_repository import get_all_users_repository
from app.schemas.user_schema import UserCreate, User
from typing import List
from app.core.database_config import get_db
from sqlalchemy.dialects.postgresql import UUID

router = APIRouter()


@router.get("", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    return get_all_users_repository(db)


@router.get("/{user_id}", response_model=User)
def get_user(user_id, db: Session = Depends(get_db)):
    return get_user_service(db, user_id)


@router.post("", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)


@router.delete("/{user_id}")
def delete_user(user_id, db: Session = Depends(get_db)):
    return delete_user_service(db, user_id)
