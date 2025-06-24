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
    pass
