from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.user_model import UserModel
from database import connection


class GetUserByIdQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, userid: str):
        stmt = (
            select(UserModel)
            .where(UserModel.userid == userid)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record

