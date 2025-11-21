from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import SessionLocal
from collections.abc import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession,None]:
    async with SessionLocal() as session:
        yield session

SessionDep = Depends(get_session)
