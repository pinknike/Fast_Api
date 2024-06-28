from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base

data_bases = "postgresql+asyncpg://postgres:postgres@localhost:5433/task_test"
engine = create_async_engine(data_bases, echo=True)

async_session_maker = sessionmaker(
    autocommit=False,
    bind=engine,
    class_=AsyncSession,
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)





