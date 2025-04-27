from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")  # Valor padrão se não definir
DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)  # Valor padrão se não definir
DATABASE_NAME = os.getenv("DATABASE_NAME", "python-api")


# Construa a URL de conexão para o PostgreSQL
DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Cria o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir os modelos
Base = declarative_base()

from sqlalchemy.orm import Session
from app.core.database_config import SessionLocal

# Função que cria e retorna uma sessão de banco de dados
def get_db():
    db = SessionLocal()  # Obtém uma instância da sessão do banco
    try:
        yield db  # Permite que a dependência seja usada
    finally:
        db.close()  # Garante que a conexão seja fechada após o uso
