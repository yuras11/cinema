from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from database import connection
from orm.cinema_session_model import CinemaSessionModel
from sqlalchemy import delete


class DeleteExpiredTicketsJob:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = delete(CinemaSessionModel).where(
            CinemaSessionModel.sessiondate < datetime.today()
        )
        await session.execute(stmt)
        await session.commit()
        return {'message': 'ok'}

