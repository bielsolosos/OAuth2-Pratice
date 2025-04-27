from app.core.database_config import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from passlib.context import CryptContext
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#SqlAlchemy é por onde define o ORM
class User(Base):
    __tablename__ = "Users"
                                                     #config para gerar UUID's
    id = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    name =  Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def set_password(self, password: str):
        """Criptografa a senha antes de salvar."""
        self.password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verifica se a senha informada corresponde à criptografada."""
        return pwd_context.verify(password, self.password)