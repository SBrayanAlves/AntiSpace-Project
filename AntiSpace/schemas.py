from pydantic import BaseModel, EmailStr

class CriarUsuarios(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class Usuario(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class config:
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    senha: str