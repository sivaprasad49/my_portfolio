import contextlib
import logging
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import postgres_settings


class PostgresDB:
    def __init__(self, pg_url: str):
        self._engine = create_async_engine(url=pg_url)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self):
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        session = self._sessionmaker()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


def init_db() -> PostgresDB:
    try:
        logging.info("Successfully connected to postgres instance")
        return PostgresDB(pg_url=postgres_settings.db_url)
    except Exception as e:
        logging.exception(
            f"Unable to connect to postgres instance, shutting down: {str(e)}"
        )
        exit(1)


db = init_db()
