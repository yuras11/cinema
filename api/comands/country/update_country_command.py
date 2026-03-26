from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.country_model import CountryModel
from api.comands.country.country_command import CountryCommand
from database import connection


class UpdateCountryCommandHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, countrycode: str, command: CountryCommand):
        stmt = (
            select(CountryModel)
            .where(CountryModel.countrycode == countrycode)
        )
        existing = await session.execute(stmt)
        country = existing.unique().scalar_one_or_none()

        if country is None:
            return None

        country.countryname = command.countryname

        try:
            await session.commit()
            await session.refresh(country)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return country
