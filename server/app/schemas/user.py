from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

# Campos comuns para todos os esquemas de usuário
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    full_name: Optional[str] = None

# Esquema de criação
class UserCreate(UserBase):
    password: str

# Esquema de atualização
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    full_name: Optional[str] = None

# Esquema de resposta
class UserResponse(UserBase):
    id: int
    is_superuser: bool
    created_at: datetime

    # Configuração para permitir a compatibilidade com ORM
    model_config = ConfigDict(from_attributes=True)