from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings
from typing import AsyncGenerator

# Criando a engine assincrona do sqlalchemy
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

# Criando a sessionmaker assincrona do sqlalchemy
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# Dependencia para obter a sessao do banco de dados
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session # Fornece a sessao para o contexto do request
        finally:
            await session.close() # Garante que a sessao feche apos o uso