from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Login
from models import Usuarios
from database import get_db

router = APIRouter()

@router.post("/login")
async def login(entrada: Login, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(
        Usuarios.email == entrada.email,
        Usuarios.senha == entrada.senha
    ).first()

    if usuario:
        return {"Mensagem": "Voce esta logado"}