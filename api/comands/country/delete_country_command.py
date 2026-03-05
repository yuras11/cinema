from orm.country_model import CountryModel
from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from repository.database import connection


class DeleteCountryCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, countrycode: str):
        stmt = (
            delete(CountryModel)
            .where(CountryModel.countrycode == countrycode)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount