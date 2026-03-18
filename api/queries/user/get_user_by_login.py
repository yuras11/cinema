from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from orm.user_model import UserModel
from repository.database import connection


class GetUserByLoginQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, userlogin: str):
        stmt = (
            select(UserModel)
            .where(UserModel.userlogin == userlogin)
        )
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records