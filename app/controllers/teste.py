from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def teste():
    return {"message": "API funcionando certinho!"}

@router.get("/{nome}")
async def olaTio(nome : str):
    return f"fala mano {nome}"