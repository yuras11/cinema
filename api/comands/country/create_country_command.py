from orm.country_model import CountryModel
from api.comands.country.country_command import CountryCommand
from database import connection
from sqlalchemy import select
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class CreateCountryCommandHandler:
    @classmethod
    async def __check_existence(cls, session, stmt, command):
        existing = await session.execute(stmt)
        if existing.unique().scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f'Country with code {command.countrycode} already exists!')


    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: CountryCommand):
        # stmt = (
        #     select(CountryModel)
        #     .where(CountryModel.countrycode == command.countrycode)
        # )
        # existing = await session.execute(stmt)
        # if existing.unique().scalar_one_or_none():
        #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        #                         detail=f'Country with code {command.countrycode} already exists!')
        stmt = (
            select(CountryModel)
            .where(CountryModel.countrycode == command.countrycode)
        )

        await cls.__check_existence(session, stmt, command)

        model = CountryModel(**command.model_dump())
        session.add(model)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return model