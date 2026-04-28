from database import connection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from exceptions.exceptions import NotFoundException
from orm.cast_member_model import CastMemberModel


class GetAllCastMembersQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(CastMemberModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        if not records:
            raise NotFoundException('Cast members have not been found!')
        return records