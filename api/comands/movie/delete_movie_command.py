from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from orm.movie_model import MovieModel
from database import connection


class DeleteMovieCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, movieid: int):
        stmt = (
            delete(MovieModel)
            .where(MovieModel.movieid == movieid)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount