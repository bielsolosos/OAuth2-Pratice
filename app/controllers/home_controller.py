from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def teste():
    return {"message": "API funcionando certinho!"}
