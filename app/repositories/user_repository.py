from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from sqlalchemy.dialects.postgresql import UUID
from fastapi import HTTPException
from app.core.execptions import (
    raise_not_found_exception,
    raise_bad_request_exception,
    raise_internal_server_error
)

def get_user_repository(db: Session, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise_not_found_exception("User not found.")
    return user

def get_user_by_email_repository(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    if user is None:
        raise_not_found_exception("User not found.")
    return user

def get_all_users_repository(db: Session):
    return db.query(User).all()

def create_user_repository(db: Session, user_data: dict):
    try:
        db_user = User(**user_data)
        db_user.set_password(user_data["password"])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise_bad_request_exception("Email já cadastrado. Tente um email diferente.")
    except Exception as e:
        db.rollback()
        raise_internal_server_error(f"An unexpected error occurred: {str(e)}")

def delete_user_repository(db: Session, user_id: UUID):
    user_to_delete = get_user_repository(db, user_id)

    try:
        db.delete(user_to_delete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise_internal_server_error(f"An unexpected error occurred: {str(e)}")
