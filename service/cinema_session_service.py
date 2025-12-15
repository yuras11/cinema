import datetime

from pydantic_schemas.cinema_session_schemas import CinemaSessionCreateScheme, CinemaSessionUpdateScheme
from repository.repos import CinemaSessionRepository
from repository.database import connection
import asyncio


class CinemaSessionService:
    @classmethod
    async def get_all_cinema_sessions(cls):
        return await CinemaSessionRepository.get_all()


    @classmethod
    async def get_todays_billboard(cls):
        return await CinemaSessionRepository.find(sessiondate=datetime.date.today())


    @classmethod
    async def get_cinema_sessions_by_date(cls, sessiondate: datetime.date):
        return await CinemaSessionRepository.find(sessiondate=sessiondate)


    @classmethod
    async def create_cinema_session(cls, session_scheme: CinemaSessionCreateScheme):
        return await CinemaSessionRepository.create_cinema_session(session_scheme=session_scheme)


    @classmethod
    async def update_cinema_session(cls, session_scheme: CinemaSessionUpdateScheme):
        return await CinemaSessionRepository.update_cinema_session(session_scheme=session_scheme)


    @classmethod
    async def delete_cinema_session(cls, sessionid: int):
        return await CinemaSessionRepository.delete(sessionid=sessionid)