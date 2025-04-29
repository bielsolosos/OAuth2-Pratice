from fastapi import APIRouter, Depends
from app.core.auth_config import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/token-test")
def test_me(current_user: User = Depends(get_current_user)):
    return {"message": f"Oi, {current_user.name}! Seu token está válido!"}