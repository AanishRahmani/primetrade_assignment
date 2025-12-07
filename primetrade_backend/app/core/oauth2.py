from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM
from app.database import get_db
from sqlalchemy import select
from app.model.user import User
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")


        if user_id is None:
            raise HTTPException(status_code=401,detail= "Invalid token")

    except JWTError:
        raise HTTPException(status_code=401,detail= "Invalid or expired token")

    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def admin_only(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403,detail= "Admins only")
    return user
