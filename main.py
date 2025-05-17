from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # <- importando CORS
from app.core.database_config import Base, engine
import app.controllers.home_controller as home_controller
import app.controllers.user_controller as user_controller
import app.controllers.auth_controller as auth_controller
import os

app = FastAPI(
    title="OAuth-pratice"
)

# Configuração do CORS - ADICIONE ISSO AQUI
origins = [
    "https://api.bielsolososdev.space",    # seu domínio customizado
    "http://localhost",
    "http://localhost:8000",
    "https://oauth2-pratice-production.up.railway.app",  # URL Railway, se quiser permitir também
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # lista de domínios liberados
    allow_credentials=True,
    allow_methods=["*"],         # libera todos os métodos (GET, POST, etc)
    allow_headers=["*"],         # libera todos os headers
)

# Conectar e criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app.include_router(home_controller.router, prefix="/home", tags=["Home"])
app.include_router(user_controller.router, prefix="/user", tags=["Users"])
app.include_router(auth_controller.router, prefix="/token", tags=["Token"])

# Esse trecho abaixo é pra quando você rodar localmente (tipo python main.py)
if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(
        "main:app",
        host="0.0.0.0",    # <---- Melhor usar 0.0.0.0 pra aceitar conexões externas
        port=int(os.environ.get("PORT", 8000)),
        reload=True
    )
