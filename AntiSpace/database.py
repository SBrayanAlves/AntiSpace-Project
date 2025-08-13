from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE")

engine = create_engine(database_url, echo=True)

Base.metadata.create_all(bind=engine)

_Sessao = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = _Sessao()
    try:
        yield db
    finally:
        db.close()