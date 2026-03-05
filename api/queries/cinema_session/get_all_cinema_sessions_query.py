from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.cinema_session_model import CinemaSessionModel
from repository.database import connection


class GetAllCinemaSessionsQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(CinemaSessionModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records