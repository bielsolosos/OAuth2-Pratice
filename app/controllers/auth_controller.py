from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user_schema import User
from app.core.database_config import get_db
from sqlalchemy.dialects.postgresql import UUID
from app.core.auth_config import create_access_token, authenticate_user, get_current_user

router = APIRouter()

#Função para pegar o Token
@router.post("/token")
def login_for_acessToken(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas",
        )
    
    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}

#Função para testar o Token
@router.get("/token-test")
def test_me(current_user: User = Depends(get_current_user)):
    return {"message": f"Oi, {current_user.name}! Seu token está válido!"}