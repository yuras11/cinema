from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import datetime
from orm.cinema_session_model import CinemaSessionModel
from orm.movie_model import MovieModel
from repository.database import connection


class GetActualMoviesQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = (
            select(MovieModel)
            .join(CinemaSessionModel)
            .where(CinemaSessionModel.sessiondate >= datetime.date.today())
        )
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records