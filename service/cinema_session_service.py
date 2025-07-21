import datetime

from pydantic_schemas.cinema_session_schemas import CinemaSessionScheme
from repository.repos import CinemaSessionRepository
from repository.database import connection
import asyncio


class CinemaSessionService:
    @classmethod
    async def get_all_cinema_sessions(cls):
        return await CinemaSessionRepository.get_all()


    @classmethod
    async def get_cinema_sessions_by_date(cls, sessiondate: datetime.date):
        return await CinemaSessionRepository.find(sessiondate=sessiondate)


    @classmethod
    async def create_cinema_session(cls, cinema_session: CinemaSessionScheme):
        return await CinemaSessionRepository.insert(cinema_session_scheme=cinema_session)


    @classmethod
    async def update_cinema_session(cls, cinema_session_scheme: CinemaSessionScheme):
        return await CinemaSessionRepository.update(
            filters={
                'movieid': cinema_session_scheme.movieid,
                'hallid': cinema_session_scheme.hallid,
                'sessiondate': cinema_session_scheme.sessiondate,
                'sessiontime': cinema_session_scheme.sessiontime
            },
            values=cinema_session_scheme.model_dump()
        )


    @classmethod
    async def delete_cinema_session(cls, cinema_session_scheme: CinemaSessionScheme):
        return await CinemaSessionRepository.delete(**cinema_session_scheme.model_dump())