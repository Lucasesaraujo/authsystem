from sqlachemy.ext.asyncio import AsyncSession
from sqlachemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

# Função para criar um novo usuário
async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(
        email=user.email,
        hashed_password=user.password,  # Hash da senha antes de salvar !!!
        full_name=user.full_name,
        is_active=user.is_active,
    )

    db.add(db_user) # Adiciona o novo usuário na sessão
    await db.commit() # Salva as mudanças no banco de dados
    await db.refresh(db_user) # Atualiza o user com os dados do banco

    return db_user

async def get_user_by_email(db: AsyncSession, email: str):
    # Consulta para buscar o usuário pelo email
    result = await db.execute(select(User).where(User.email == email))

    return result.scalars().first()  # Retorna o primeiro usuário encontrado ou None