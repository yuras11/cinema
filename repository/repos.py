from http.client import HTTPException

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete


from orm.cast_member_model import CastMemberModel, ProfessionModel
from orm.cinema_session_model import CinemaSessionModel
from orm.country_model import CountryModel
from orm.hall_model import HallModel, SeatModel, SeatStatusModel
from orm.movie_model import MovieModel, GenreModel, movie_countries
from orm.user_model import UserModel
from pydantic_schemas.cast_member_schemas import CastMemberCreateScheme
from pydantic_schemas.cinema_session_schemas import CinemaSessionCreateScheme, CinemaSessionUpdateScheme
from pydantic_schemas.country_schemas import CountryScheme
from pydantic_schemas.hall_schemas import HallCreateScheme, HallUpdateScheme
from pydantic_schemas.movie_schemas import MovieScheme, MovieUpdateScheme
from repository.base_repository import Repository
from repository.database import connection


class CountryRepository(Repository):
    model = CountryModel


class UserRepository(Repository):
    model = UserModel


class CastMemberRepository(Repository):
    model = CastMemberModel


class MovieRepository(Repository):
    model = MovieModel

    @classmethod
    @connection
    async def create_movie(cls, session: AsyncSession, movie_scheme: MovieScheme):
        movie = MovieModel(
            moviename=movie_scheme.moviename,
            durationtime=movie_scheme.durationtime,
            releaseyear=movie_scheme.releaseyear,
            agerate=movie_scheme.agerate
        )

        genres = await session.execute(
            select(GenreModel).where(GenreModel.genreid.in_(movie_scheme.genres))
        )
        countries = await session.execute(
            select(CountryModel).where(CountryModel.countrycode.in_(movie_scheme.countries))
        )
        cast_members = await session.execute(
            select(CastMemberModel).where(CastMemberModel.memberid.in_(movie_scheme.cast))
        )

        movie.genres = list(genres.scalars().unique().all())
        movie.countries = list(countries.scalars().unique().all())
        movie.cast_members = list(cast_members.scalars().unique().all())

        session.add(movie)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return movie

    @classmethod
    @connection
    async def update_movie(cls, session: AsyncSession, movie_scheme: MovieUpdateScheme):
        result = await session.execute(
            select(MovieModel).where(MovieModel.movieid==movie_scheme.movieid)
        )

        movie = result.unique().scalar_one_or_none()

        if movie is None:
            return None

        movie.moviename = movie_scheme.moviename
        movie.agerate = movie_scheme.agerate
        movie.durationtime = movie_scheme.durationtime
        movie.releaseyear = movie_scheme.releaseyear

        if movie_scheme.genres is not None:
            genres = await session.execute(
                select(GenreModel).where(GenreModel.genreid.in_(movie_scheme.genres))
            )
            movie.genres = list(genres.scalars().unique().all())

        if movie_scheme.countries is not None:
            countries = await session.execute(
                select(CountryModel).where(CountryModel.countrycode.in_(movie_scheme.countries))
            )
            movie.countries = list(countries.scalars().unique().all())

        if movie_scheme.cast is not None:
            cast_members = await session.execute(
                select(CastMemberModel).where(CastMemberModel.memberid.in_(movie_scheme.cast))
            )
            movie.cast_members = list(cast_members.scalars().unique().all())

        await session.commit()
        await session.refresh(movie)
        return movie


class HallRepository(Repository):
    model = HallModel

    @classmethod
    @connection
    async def create_hall(cls, session: AsyncSession, hall_scheme: HallCreateScheme):
        hall = HallModel(**hall_scheme.model_dump())
        session.add(hall)
        await session.flush() # this is for getting hall's id before commiting to DB

        for row in range(hall_scheme.rowamount):
            for seat in range(hall_scheme.seatamount):
                seat_model = SeatModel(
                    hallid = hall.hallid,
                    rownumber = row + 1,
                    seatnumber = seat + 1
                )
                session.add(seat_model)

        await session.commit()
        return hall


    @classmethod
    @connection
    async def update_hall(cls, session: AsyncSession, hall_scheme: HallUpdateScheme):
        result = await session.execute(
            select(HallModel).where(HallModel.hallid==hall_scheme.hallid)
        )
        hall = result.unique().scalar_one_or_none()

        if hall is None:
            return None

        hall.hallname = hall_scheme.hallname

        rows_changed = hall.rowamount != hall_scheme.rowamount
        seats_changed = hall.seatamount != hall_scheme.seatamount

        if rows_changed or seats_changed:
            hall.rowamount = hall_scheme.rowamount
            hall.seatamount = hall_scheme.seatamount

            await session.execute(
                delete(SeatModel).where(SeatModel.hallid == hall.hallid)
            )

            for row in range(hall_scheme.rowamount):
                for seat in range(hall_scheme.seatamount):
                    seat_model = SeatModel(
                        hallid=hall.hallid,
                        rownumber=row + 1,
                        seatnumber=seat + 1
                    )
                    session.add(seat_model)

        await session.commit()
        return hall


class CinemaSessionRepository(Repository):
    model = CinemaSessionModel

    @classmethod
    @connection
    async def create_cinema_session(cls, session: AsyncSession, session_scheme: CinemaSessionCreateScheme):
        cinema_session = CinemaSessionModel(**session_scheme.model_dump())
        result = await session.execute(
            select(HallModel).where(HallModel.hallid==cinema_session.hallid)
        )
        cinema_session.hall = result.unique().scalar_one_or_none()
        session.add(cinema_session)
        await session.flush()

        for row in range(1, cinema_session.hall.rowamount + 1):
            for seat in range(1, cinema_session.hall.seatamount + 1):
                seat_status = SeatStatusModel(
                    sessionid=cinema_session.sessionid,
                    hallid=cinema_session.hallid,
                    rownumber=row,
                    seatnumber=seat
                )
                session.add(seat_status)

        await session.commit()
        return cinema_session
        

    @classmethod
    @connection
    async def update_cinema_session(cls, session: AsyncSession, session_scheme: CinemaSessionUpdateScheme):
        result = await session.execute(
            select(CinemaSessionModel).where(CinemaSessionModel.sessionid==session_scheme.sessionid)
        )
        cinema_session = result.unique().scalar_one_or_none()

        if cinema_session is None:
            return None

        result = await session.execute(
            select(HallModel).where(HallModel.hallid == cinema_session.hallid)
        )
        cinema_session.hall = result.unique().scalar_one_or_none()

        result = await session.execute(
            select(HallModel).where(HallModel.hallid == session_scheme.hallid)
        )
        hall = result.unique().scalar_one_or_none()

        await session.execute(
            delete(SeatStatusModel).where(
                SeatStatusModel.hallid == cinema_session.hallid,
                SeatStatusModel.sessionid == cinema_session.sessionid
            )
        )

        cinema_session.movieid = session_scheme.movieid
        cinema_session.hallid = session_scheme.hallid
        cinema_session.sessiondate = session_scheme.sessiondate
        cinema_session.sessiontime = session_scheme.sessiontime
        cinema_session.ticketfee = session_scheme.ticketfee
        cinema_session.currencycode = session_scheme.currencycode

        for row in range(1, hall.rowamount + 1):
            for seat in range(1, hall.seatamount + 1):
                seat_status = SeatStatusModel(
                    sessionid=session_scheme.sessionid,
                    hallid=session_scheme.hallid,
                    rownumber=row,
                    seatnumber=seat
                )
                session.add(seat_status)

        await session.commit()
        return cinema_session

