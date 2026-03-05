from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import load_only

from orm.cast_member_model import CastMemberModel
from orm.country_model import CountryModel
from orm.movie_model import MovieModel, GenreModel
from fastapi import HTTPException, status
from pydantic_schemas.movie_schemas import MovieCommand
from repository.database import connection


class CreateMovieCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: MovieCommand):
        stmt = (
            select(MovieModel)
            .where(MovieModel.moviename == command.moviename)
        )
        existing = await session.execute(stmt)
        if existing.unique().scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f'Movie with name {command.moviename} already exists!')

        movie = MovieModel(
            moviename=command.moviename,
            durationtime=command.durationtime,
            releaseyear=command.releaseyear,
            agerate=command.agerate
        )

        genre_ids = command.genres or []
        country_codes = command.countries or []
        cast_ids = command.cast or []

        if genre_ids:
            genres = await session.execute(
                select(GenreModel)
                .options(load_only(GenreModel.genreid))
                .where(GenreModel.genreid.in_(genre_ids))
            )
            movie.genres = genres.scalars().unique().all()

        if country_codes:
            countries = await session.execute(
                select(CountryModel)
                .options(load_only(CountryModel.countrycode))
                .where(CountryModel.countrycode.in_(country_codes))
            )
            movie.countries = countries.scalars().unique().all()

        if cast_ids:
            cast_members = await session.execute(
                select(CastMemberModel)
                .options(load_only(CastMemberModel.memberid))
                .where(CastMemberModel.memberid.in_(cast_ids))
            )
            movie.cast_members = cast_members.scalars().unique().all()

        # movie.genres = list(genres.scalars().unique().all())
        # movie.countries = list(countries.scalars().unique().all())
        # movie.cast_members = list(cast_members.scalars().unique().all())

        session.add(movie)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return movie