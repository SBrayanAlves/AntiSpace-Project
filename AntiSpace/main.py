from fastapi import FastAPI
from routers import users, auth

app = FastAPI(title="AntiSpace")

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
async def raiz():
    return {"mensagem": "Bem-vindo ao AntiSpace!"}