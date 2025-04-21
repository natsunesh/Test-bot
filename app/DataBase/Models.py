from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from datetime import datetime

engine = create_async_engine(url='sqlite+aiosqlite:///db.info_users')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    balance: Mapped[int] = mapped_column()
    number = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
