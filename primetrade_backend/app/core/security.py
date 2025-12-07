import datetime
from passlib.context import CryptContext
from datetime import timedelta
from jose import jwt
from dotenv import load_dotenv
import os
from typing import cast
load_dotenv()

SECRET_KEY :str= cast(str, os.getenv("JWT_SECRET_KEY"))
if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set in the environment!")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _truncate_password(password: str) -> str:
    """
    bcrypt only supports passwords up to 72 bytes.
    Truncate safely without breaking UTF-8.
    """
    return password.encode("utf-8")[:72].decode("utf-8", errors="ignore")


def hash_password(password: str) -> str:
    password = _truncate_password(password)
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = _truncate_password(plain_password)
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Generates a JWT token with an expiration time.
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.UTC) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
