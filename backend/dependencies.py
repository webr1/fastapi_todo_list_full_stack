from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import SessionLocal
from collections.abc import AsyncGenerator

"""
get_session создаёт и отдаёт (yield) асинхронную сессию базы данных.
FastAPI вызывает эту функцию каждый раз, когда роуту нужна сессия.

AsyncGenerator = функция-генератор, которая:
- открывает сессию перед запросом
- автоматически закрывает её после завершения
"""

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

# SessionDep — зависимость, которую можно использовать в любом роуте
SessionDep = Depends(get_session)
