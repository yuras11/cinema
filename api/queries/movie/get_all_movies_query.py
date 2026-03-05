from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.movie_model import MovieModel
from repository.database import connection


class GetAllMoviesQueryHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(MovieModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records