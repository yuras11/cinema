from orm.hall_model import HallModel
from sqlalchemy import select
from database import connection
from sqlalchemy.ext.asyncio import AsyncSession


class GetHallByIdQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, hallid: int):
        stmt = (
            select(HallModel)
            .where(HallModel.hallid == hallid)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record
