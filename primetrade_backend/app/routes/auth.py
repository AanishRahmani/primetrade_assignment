from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut)
async def register(data: UserCreate, db=Depends(get_db)):

    exists = await db.execute(select(User).where(User.email == data.email))
    if exists.scalar_one_or_none():
        raise HTTPException(400, "Email already exists")

    user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.post("/login")
async def login(data: UserLogin, db=Depends(get_db)):

    user = await db.execute(select(User).where(User.email == data.email))
    user = user.scalar_one_or_none()

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token, "token_type": "bearer"}
