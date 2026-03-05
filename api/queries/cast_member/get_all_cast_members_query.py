from repository.database import connection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.cast_member_model import CastMemberModel


class GetAllCastMembersQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(CastMemberModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records