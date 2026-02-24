from passlib.context import CryptContext ## library for hashing and verify password
from jose import JWTError, jwt  ## library for jwt token
from datetime import datetime, timedelta
import os
SECRET_KEY=os.getenv("SECRET_KEY", "your_secret_key")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
ALGORITHM="HS256"

pwd_context=CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
