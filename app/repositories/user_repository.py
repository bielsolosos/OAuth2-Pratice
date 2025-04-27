from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from sqlalchemy.dialects.postgresql import UUID
from fastapi import HTTPException


def get_user_repository(db: Session, user_id: UUID):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found.")

        return user
    except Exception as e:
        # Lança uma exceção HTTP para erros inesperados
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


def get_user_by_email_repository(db: Session, user_email: str):
    try:
        user = db.query(User).filter(User.email == user_email).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found.")

        return user
    except Exception as e:
        # Lança uma exceção HTTP para erros inesperados
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


def get_all_users_repository(db: Session):
    return db.query(User).all()


def create_user_repository(db: Session, user_data: dict):
    try:
        db_user = User(**user_data)
        db_user.set_password(user_data["password"])
        db.add(db_user)
        db.commit()
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Email já cadastrado. Tente um email diferente."
        )


def delete_user_repository(db: Session, user_id: UUID):
    # Tenta pegar o usuário. Se não existir, lançará a exceção dentro da função.
    user_to_delete = get_user_repository(db, user_id)

    try:
        db.delete(user_to_delete)  # Deleta o usuário
        db.commit()  # Faz commit da transação
        return True
    except Exception as e:
        db.rollback()  # Caso haja erro, desfaz a transação
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
