from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from orm.country_model import CountryModel
from repository.database import connection


class GetAllCountriesQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession):
        stmt = select(CountryModel)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records