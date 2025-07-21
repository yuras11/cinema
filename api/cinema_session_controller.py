import datetime
from sys import prefix

from fastapi import APIRouter
from typing import Optional, List

from pydantic_schemas.cinema_session_schemas import CinemaSessionScheme
from service.cinema_session_service import CinemaSessionService


cinema_session_router = APIRouter(prefix='/cinema_sessions', tags=['Working with cinema sessions'])

@cinema_session_router.get('/all')
async def get_all_cinema_sessions():
    cinema_sessions = await CinemaSessionService.get_all_cinema_sessions()
    return [cinema_session.model_dump() for cinema_session in [CinemaSessionScheme.model_validate(c) for c in cinema_sessions]]


@cinema_session_router.post('/create_cinema_session')
async def create_cinema_session(cinema_session: CinemaSessionScheme):
    result = await CinemaSessionService.create_cinema_session(cinema_session=cinema_session)
    return {'message': 'Cinema session has been successfully created'} if result else {'message': 'Error'}


@cinema_session_router.put('/update_cinema_session')
async def update_cinema_session(cinema_session: CinemaSessionScheme):
    result = await CinemaSessionService.update_cinema_session(cinema_session_scheme=cinema_session)
    return {'message': 'Cinema session has been successfully updated'} if result else {'message': 'Error'}


@cinema_session_router.delete('/delete_cinema_session')
async def delete_cinema_session(cinema_session: CinemaSessionScheme):
    result = await CinemaSessionService.delete_cinema_session(cinema_session_scheme=cinema_session)
    return {'message': 'Cinema session has been successfully updated'} if result else {'message': 'Error'}