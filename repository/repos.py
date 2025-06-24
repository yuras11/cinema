from http.client import HTTPException

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, join, update, delete
from typing import List

from sqlalchemy.orm import selectinload

from orm.cast_member_model import CastMemberModel, CastMemberNameModel, PositionModel
from orm.cinema_session_model import CinemaSessionModel
from orm.country_model import CountryModel, CountryNameModel
from orm.hall_model import HallModel, HallNameModel, SeatModel
from orm.movie_model import MovieModel, MovieNameModel, GenreModel, movie_countries
from orm.user_model import UserModel
from pydantic_schemas.cast_member_schemas import CastMemberScheme, CastMemberCreateScheme
from pydantic_schemas.country_schemas import CountryScheme, CountryNameScheme
from pydantic_schemas.hall_schemas import HallCreateScheme
from pydantic_schemas.movie_schemas import MovieScheme
from repository.base_repository import Repository
from repository.database import connection


class UserRepository(Repository):
    model = UserModel


class MovieRepository(Repository):
    model = MovieModel

    @classmethod
    @connection
    async def insert(cls, session: AsyncSession, movie_scheme: MovieScheme):
        movie = MovieModel(
            movieid=movie_scheme.movieid,
            agerate=movie_scheme.agerate,
            durationtime=movie_scheme.durationtime,
            releasedate=movie_scheme.releasedate
        )

        movie_names = [MovieNameModel(**m.model_dump()) for m in movie_scheme.names]
        movie.names = movie_names

        countries = await session.execute(
            select(CountryModel)
            .where(CountryModel.countrycode.in_([c.countrycode for c in movie_scheme.countries]))
        )
        movie.countries = countries.scalars().unique().all()

        genres = await session.execute(
            select(GenreModel)
            .where(GenreModel.genreid.in_([g.genreid for g in movie_scheme.genres]))
        )
        movie.genres = genres.scalars().unique().all()

        session.add(movie)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return movie


    @classmethod
    async def update_movie(cls, movie_scheme: MovieScheme):
        total_rowcount = 0
        total_rowcount += await cls.update(filters={'movieid': movie_scheme.movieid})
        total_rowcount += await cls.update_movie_names(movie_scheme=movie_scheme)
        total_rowcount += await cls.update_movie_countries(movie_scheme=movie_scheme)




    @classmethod
    @connection
    async def update_movie_names(cls, session: AsyncSession, movie_scheme: MovieScheme):
        statements = []
        for name in movie_scheme.names:
            stmt = (
                update(MovieNameModel)
                .where(MovieNameModel.movieid==name.movieid, MovieNameModel.languagecode==name.languagecode)
                .values(moviename=name.moviename)
                .execution_options(synchronize_session="fetch")
            )
            statements.append(stmt)
        try:
            rowcount = 0
            for stmt in statements:
                result = await session.execute(stmt)
                rowcount += result.rowcount
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return rowcount


    @classmethod
    @connection
    async def update_movie_countries(cls, session: AsyncSession, movie_scheme: MovieScheme):
        movie = await session.get(MovieModel, movie_scheme.movieid, options=[selectinload(MovieModel.countries)])
        if not movie:
            raise ValueError("Movie not found")

        current_country_codes = {country.countrycode for country in movie.countries}
        new_country_codes = {country.countrycode for country in movie_scheme.countries}

        country_codes_to_add = new_country_codes - current_country_codes
        country_codes_to_remove = current_country_codes - new_country_codes

        rowcount_to_return = 0

        if country_codes_to_remove:
            stmt = (
                delete(movie_countries)
                .where(
                    movie_countries.c.movieid == movie_scheme.movieid,
                    movie_countries.c.countrycode.in_(country_codes_to_remove)
                )
            )
            result = await session.execute(stmt)
            rowcount_to_return += result.rowcount

        if country_codes_to_add:
            countries_to_add = await session.execute(
                select(CountryModel).where(CountryModel.countrycode.in_(country_codes_to_add))
            )
            for country in countries_to_add:
                movie.countries.append(country)
                rowcount_to_return += 1

        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return rowcount_to_return


class HallRepository(Repository):
    model = HallModel

    @classmethod
    @connection
    async def insert(cls, session: AsyncSession, hall_scheme: HallCreateScheme):
        hall = HallModel(hallid=hall_scheme.hallid)
        hall_names = [HallNameModel(**h.model_dump()) for h in hall_scheme.names]
        seats = []
        for i in range(hall_scheme.row_amount):
            for j in range(hall_scheme.seat_amount // hall_scheme.row_amount):
                seats.append(
                    SeatModel(
                        hallid=hall_scheme.hallid,
                        rownumber=i+1,
                        seatnumber=j+1
                    )
                )
        hall.names = hall_names
        hall.seats = seats
        session.add(hall)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return hall


class CastMemberRepository(Repository):
    model = CastMemberModel

    @classmethod
    @connection
    async def insert(cls, session: AsyncSession, cast_member_scheme: CastMemberCreateScheme):
        cast_member = CastMemberModel(
            memberid=cast_member_scheme.memberid,
            dateofbirth=cast_member_scheme.dateofbirth,
            countrycode=cast_member_scheme.countrycode
        )

        cast_member_country = await session.get(CountryModel, cast_member_scheme.countrycode)
        cast_member.country = cast_member_country
        cast_member.countrycode = cast_member_scheme.countrycode

        cast_member_names = [
            CastMemberNameModel(
                memberid=name.memberid,
                languagecode=name.languagecode,
                membername=name.membername
            )
            for name in cast_member_scheme.names
        ]
        cast_member.names = cast_member_names

        res = await session.execute(
            select(PositionModel).where(PositionModel.positionid.in_([pos.positionid for pos in cast_member_scheme.positions]))
        )
        cast_member_positions = res.scalars().unique().all()
        cast_member.positions = cast_member_positions

        session.add(cast_member)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return cast_member


class CinemaSessionRepository(Repository):
    model = CinemaSessionModel


class CountryRepository(Repository):
    model = CountryModel

    @classmethod
    @connection
    async def insert(cls, session: AsyncSession, country_model: CountryScheme):
        country = CountryModel(countrycode=country_model.countrycode)
        country.names = [CountryNameModel(**name.model_dump()) for name in country_model.names]
        session.add(country)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return country


    @classmethod
    @connection
    async def update_name(cls, session: AsyncSession, country_name_scheme: CountryNameScheme):
        stmt = (
            update(CountryNameModel)
            .where(CountryNameModel.countrycode == country_name_scheme.countrycode,
                   CountryNameModel.languagecode == country_name_scheme.languagecode)
            .values(countryname=country_name_scheme.countryname)
        )

        result = await session.execute(stmt)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount


    @classmethod
    @connection
    async def add_name(cls, session: AsyncSession, country_name: CountryNameScheme):
        country = await session.get(CountryModel, country_name.countrycode)
        if not country:
            raise HTTPException(status_code=404, detail='Country not found')
        existing_name = await session.get(
            CountryNameModel,
            (country_name.countrycode, country_name.languagecode)
        )
        if existing_name:
            raise HTTPException(status_code=409, detail='Such name already exists')

        country_name_model = CountryNameModel(**country_name.model_dump())
        session.add(country_name_model)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return country_name_model