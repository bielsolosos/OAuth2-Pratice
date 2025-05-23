from fastapi import FastAPI # type: ignore
from app.core.database_config import Base, engine
import app.controllers.home_controller as home_controller
import app.controllers.user_controller as user_controller
import app.controllers.auth_controller as auth_controller
import os

app = FastAPI(
    title="OAuth-pratice"
)
# Conectar e criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app.include_router(home_controller.router, prefix="/home", tags=["Home"])
app.include_router(user_controller.router, prefix="/user", tags=["Users"])
app.include_router(auth_controller.router, prefix="/token", tags=["Token"],)



# Esse trecho abaixo é pra quando você rodar localmente (tipo python main.py)
if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=int(os.environ.get("PORT", 8000)),
        reload=True
    )
