from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import CriarUsuarios
from models import Usuarios
from database import get_db

router = APIRouter()

@router.post("/cadastro")
async def criar_usuario(usuario: CriarUsuarios, db: Session = Depends(get_db)):
    cadastro = Usuarios(
        nome = usuario.nome,
        email = usuario.email,
        senha = usuario.senha
    )
    db.add(cadastro)
    db.commit()
    db.refresh(cadastro)

    return {f"Mensagem": "Usuario criado com sucesso! Bem vindo {usuario.nome}!"}