from app.repositories.user_repository import get_user_repository, create_user_repository, delete_user_repository
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.user_schema import UserCreate


def get_user_service(db: Session, user_id: UUID):
    return get_user_repository(db, user_id)


def create_user_service(db: Session, user_data: UserCreate):
    return create_user_repository(db, user_data.model_dump())

def delete_user_service(db: Session, user_id: UUID):
    delete_user_repository(db, user_id)