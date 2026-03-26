from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.movie_model import MovieModel
from database import connection


class GetMovieByIdQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, movieid: int):
        stmt = (
            select(MovieModel)
            .where(MovieModel.movieid == movieid)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record