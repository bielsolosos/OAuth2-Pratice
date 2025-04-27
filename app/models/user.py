from app.core.database_config import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

#SqlAlchemy é por onde define o ORM
class User(Base):
    __tablename__ = "Users"
                                                     #config para gerar UUID's
    id = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    name =  Column(String)
    email = Column(String, unique=True)