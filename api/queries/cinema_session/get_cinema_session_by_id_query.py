from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from orm.cinema_session_model import CinemaSessionModel
from database import connection


class GetCinemaSessionByIdQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, sessionid: int):
        stmt = (
            select(CinemaSessionModel)
            .where(CinemaSessionModel.sessionid == sessionid)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record