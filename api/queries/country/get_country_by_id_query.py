from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from orm.country_model import CountryModel
from repository.database import connection


class GetCountryByIdQueryHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, countrycode: str):
        stmt = (
            select(CountryModel)
            .where(CountryModel.countrycode == countrycode)
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record
