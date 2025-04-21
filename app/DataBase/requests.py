from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .Models import User, async_session
from datetime import datetime

async def add_user(user_id: int, number: int):
    async with async_session() as session:
        async with session.begin():
            existing_user = await get_user(user_id)
            if existing_user:
                raise ValueError(f"User with user_id {user_id} already exists.")
            user = User(user_id=user_id, balance=0, number=number, created_at=datetime.utcnow())
            session.add(user)

async def get_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).filter_by(user_id=user_id).order_by(User.created_at.desc()))
        return result.scalar_one_or_none()

async def update_user(user: User):
    async with async_session() as session:
        async with session.begin():
            session.add(user)
            await session.commit()
