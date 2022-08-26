from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .. import settings

Base = declarative_base()

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.DB_USERNAME}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    future=True,
    echo=False,
    pool_size=10,
    pool_timeout=30
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


from .item_model import Item