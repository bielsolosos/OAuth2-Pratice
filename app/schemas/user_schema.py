from pydantic import BaseModel
from uuid import UUID  # Classe de UUID

# Esse arquivo serve para serializar/deserializar para o Banco de dados/json no sistema.


# Classe base, é o nosso "DTO" que serve fazermos os posts, tem que herdar de BaseModel
class UserBase(BaseModel):
    name: str
    email: str


# Herda a Classe base e é usada para a validação de entrada, como posts por exemplo
class UserCreate(UserBase):
    password: str  # Adicionando a senha aqui

    class Config:
        orm_mode = True


class User(UserBase):
    id: UUID

    class Config:
        orm_mode = (
            True  # Permite que o Pydantic converta modelos SQLAlchemy para esquemas
        )
