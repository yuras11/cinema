from pydantic_schemas.cinema_session_schemas import CinemaSessionScheme
from repository.repos import CinemaSessionRepository
from repository.database import connection
import asyncio


class CinemaSessionService:
    @classmethod
    async def get_all_cinema_sessions(cls):
        return await CinemaSessionRepository.get_all()

    @classmethod
    async def get_cinema_sessions_by_date(cls, sessiondate):
        return await CinemaSessionRepository.find(sessiondate=sessiondate)

# cinema_sessions = asyncio.get_event_loop().run_until_complete(CinemaSessionService.get_all_cinema_sessions())
# for cinema_session in cinema_sessions:
#     cinema_session_p = CinemaSessionScheme.model_validate(cinema_session)
#     print(cinema_session_p.model_dump_json())