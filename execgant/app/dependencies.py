from typing import AsyncGenerator

from app.clients.db import db
from app.services.ml_service import MLService, ml_service


async def get_db_session() -> AsyncGenerator:
    async with db.session() as session:
        yield session


async def get_ml_service() -> MLService:
    return ml_service