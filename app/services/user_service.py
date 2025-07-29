from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate
from sqlalchemy import select

async def create_user(db: AsyncSession, user: UserCreate):
    pass
