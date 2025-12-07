from __future__ import annotations
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://admin:password@localhost:5432/mydb"


class Base(DeclarativeBase):
    pass


# create async engine
engine = create_async_engine(DATABASE_URL, echo=True)


# create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)


# dependency used in routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


# initialize database tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
