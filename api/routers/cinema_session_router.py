from fastapi import APIRouter

from api.comands.cinema_session.create_cinema_session_command import CreateCinemaSessionCommandHandler
from api.comands.cinema_session.update_cinema_session_command import UpdateCinemaSessionCommandHandler
from api.comands.cinema_session.delete_cinema_session_command import DeleteCinemaSessionCommandHandler
from api.queries.cinema_session.get_all_cinema_sessions_query import GetAllCinemaSessionsQueryHandler
from api.queries.cinema_session.get_cinema_session_by_id_query import GetCinemaSessionByIdQueryHandler
from pydantic_schemas.cinema_session_schemas import CinemaSessionCommand

test_cs_router = APIRouter(prefix='/test_cinema_sessions', tags=["cinema_sessions"])


@test_cs_router.get('/')
async def get_all_cinema_sessions():
    cinema_sessions = await GetAllCinemaSessionsQueryHandler.handle_async()
    return [cm.to_dict() for cm in cinema_sessions]


@test_cs_router.get('/{sessionid}')
async def get_cinema_session_by_id(sessionid: int):
    cinema_session = await GetCinemaSessionByIdQueryHandler.handle_async(sessionid=sessionid)
    return cinema_session.to_dict()


@test_cs_router.post('/')
async def create_cinema_session(command: CinemaSessionCommand):
    result = await CreateCinemaSessionCommandHandler.handle_async(command=command)
    return {'message': "cinema session is successfully created"} if result else {'message': 'error'}


@test_cs_router.put('/{sessionid}')
async def update_cinema_session(sessionid: int, command: CinemaSessionCommand):
    result = await UpdateCinemaSessionCommandHandler.handle_async(sessionid=sessionid, command=command)
    return {'message': "cinema session is successfully updated"} if result else {'message': 'error'}


@test_cs_router.delete('/{sessionid}')
async def delete_cinema_session(sessionid: int):
    result = await DeleteCinemaSessionCommandHandler.handle_async(sessionid=sessionid)
    return {'message': "cinema session is successfully deleted"} if result else {'message': 'error'}