from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from orm.movie_model import MovieModel, GenreModel
from orm.country_model import CountryModel
from orm.cast_member_model import CastMemberModel
from api.comands.movie.movie_command import MovieCommand
from database import connection


class UpdateMovieCommandHandler:
    
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, movieid: int, command: MovieCommand):
        result = await session.execute(
            select(MovieModel)
            .options(
                selectinload(MovieModel.genres),
                selectinload(MovieModel.countries),
                selectinload(MovieModel.cast_members),
            )
            .where(MovieModel.movieid == movieid)
        )

        movie = result.scalar_one_or_none()

        if movie is None:
            return None

        movie.moviename = command.moviename
        movie.agerate = command.agerate
        movie.durationtime = command.durationtime
        movie.releaseyear = command.releaseyear

        if command.genres is not None:
            genres = await session.execute(
                select(GenreModel).where(GenreModel.genreid.in_(command.genres))
            )
            movie.genres = genres.scalars().unique().all()

        if command.countries is not None:
            countries = await session.execute(
                select(CountryModel).where(CountryModel.countrycode.in_(command.countries))
            )
            movie.countries = countries.scalars().unique().all()

        if command.cast is not None:
            cast_members = await session.execute(
                select(CastMemberModel).where(CastMemberModel.memberid.in_(command.cast))
            )
            movie.cast_members = cast_members.scalars().unique().all()

        try:
            await session.commit()
            await session.refresh(movie)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return movie