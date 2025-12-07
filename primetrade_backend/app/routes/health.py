from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database import AsyncSessionLocal

router = APIRouter(prefix="/api/v1", tags=["Health"])


@router.get("/health")
async def health_check():
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
        db_status = "healthy"
    except SQLAlchemyError:
        db_status = "unhealthy"

    return {"status": "ok", "database": db_status}
