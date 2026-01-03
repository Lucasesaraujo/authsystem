from passlib.context import CryptContext

# Configura o algoritmo de hash (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Recebe senha pura e retorna o hash criptografado."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha bate com o hash (usaremos no Login)."""
    return pwd_context.verify(plain_password, hashed_password)