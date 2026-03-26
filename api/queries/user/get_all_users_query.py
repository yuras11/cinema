from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.user_model import UserModel
from database import connection


class GetAllUsersQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(UserModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records
