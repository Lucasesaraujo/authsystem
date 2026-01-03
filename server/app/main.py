from fastapi import FastAPI
# 1. Importamos o arquivo que contém a rota de registro
from server.app.api.v1.endpoints import auth

app = FastAPI(title="Auth System")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "O servidor está rodando! 🚀"}