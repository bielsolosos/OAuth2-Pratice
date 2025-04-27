# app/core/auth_config.py
from datetime import datetime, timedelta, timezone
from typing import Union
from jose import JWTError, jwt, ExpiredSignatureError
from app.schemas.user_schema import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.repositories.user_repository import (
    get_user_by_email_repository,
    get_user_repository,
)
from app.core.database_config import get_db
from dotenv import load_dotenv
import os

load_dotenv()

# Configurações para o JWT
SECRET_KEY = os.getenv("SECRET_KEY", "key_secreta")  # Substitua por uma chave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_MINUTES", 120)
)  # Tempo de expiração

# Inicializa o esquema de OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Inicia o contexto de criptografia com bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """Verifica se a senha informada corresponde à senha criptografada"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Retorna a senha criptografada"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """Cria o token JWT com data de expiração"""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expire = datetime.now(tz=timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def authenticate_user(db, email: str, password: str):
    """Autentica o usuário, retornando o usuário se a senha for válida"""
    user = get_user_by_email_repository(db, email)
    if not user or not verify_password(password, user.password):
        return False
    return user


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Valida o token e retorna o usuário correspondente"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        db = next(get_db())  # <- PEGA O DB MANUALMENTE
        user = get_user_repository(db, user_id)

        if user is None:
            raise credentials_exception

        return user
    except JWTError:
        # Em caso de erro na decodificação do token (por exemplo, token inválido)
        raise credentials_exception
    except ExpiredSignatureError:
        # Caso a assinatura do token tenha expirado
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        # Caso outro erro inesperado ocorra
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
