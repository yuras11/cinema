import datetime

from fastapi import APIRouter
from typing import Optional
from service.cinema_session_service import CinemaSessionService


cinema_session_router = APIRouter()

@cinema_session_router.get('/cinema_sessions')
def get_cinema_sessions_by_date(date: Optional[datetime.date] = None):
    cinema_session_service = CinemaSessionService()
    if date is None:
        return [(c.movie.names[0].moviename.strip(), c.hall.names[0].hallname.strip(), c.sessiondate, c.sessiontime) for c in cinema_session_service.get_all()]
    return [(c.movie.names[0].moviename.strip(), c.hall.names[0].hallname.strip(), c.sessiondate, c.sessiontime) for c in cinema_session_service.get_by_date(date)]
