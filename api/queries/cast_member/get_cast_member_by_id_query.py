from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from orm.cast_member_model import CastMemberModel
from database import connection


class GetCastMemberByIdQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, memberid: int):
        stmt = (
            select(CastMemberModel)
            .where(CastMemberModel.memberid == memberid)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record