from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from orm.hall_model import HallModel
from database import connection


class GetAllHallsQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(HallModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records