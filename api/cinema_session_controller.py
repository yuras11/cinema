from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from dependencies import get_current_user, get_current_admin_user
from orm.user_model import UserModel
from pydantic_schemas.cinema_session_schemas import CinemaSessionCreateScheme, CinemaSessionUpdateScheme, \
    SeatBookingRequest
from service.cinema_session_service import CinemaSessionService
from service.hall_service import HallService

cinema_session_router = APIRouter(prefix='/cinema_sessions', tags=['Working with cinema sessions'])
templates = Jinja2Templates(directory='templates')

@cinema_session_router.get('/all')
async def get_all_cinema_sessions():
    movies = await CinemaSessionService.get_all_cinema_sessions()
    return [c.model_dump() for c in
            [CinemaSessionUpdateScheme.model_validate(c) for c in movies]]


@cinema_session_router.get('/create')
async def create_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cinema_session/session_creation.html',
                                          context={'request': request})


@cinema_session_router.post('/create')
async def create_cinema_session(session_scheme: CinemaSessionCreateScheme):
    result = await CinemaSessionService.create_cinema_session(session_scheme=session_scheme)
    return {'message': 'Cinema session has been successfully created'} if result else {'message': 'Error'}


@cinema_session_router.get('/update')
async def update_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cinema_session/session_update.html',
                                          context={'request': request})


@cinema_session_router.put('/update')
async def update_cinema_session(session_scheme: CinemaSessionUpdateScheme):
    result = await CinemaSessionService.update_cinema_session(session_scheme=session_scheme)
    return {'message': 'Cinema session has been successfully updated'} if result else {'message': 'Error'}


@cinema_session_router.get('/delete')
async def update_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                          context={'request': request,
                                                   'entity': 'cinema_sessions'
                                                   })


@cinema_session_router.delete('/delete')
async def delete_cinema_session(cinema_sessionid: int):
    result = await CinemaSessionService.delete_cinema_session(sessionid=cinema_sessionid)
    return {'message': 'Cinema session has been successfully deleted'} if result else {'message': 'Error'}


@cinema_session_router.get('/booking/{sessionid}')
async def ticket_booking(sessionid: int,
                         request: Request):
    session = await CinemaSessionService.get_cinema_session_by_id(sessionid=sessionid)
    hall = await HallService.get_hall_by_id(hallid=session.hallid)
    seat_statuses_map = {
        (s.rownumber, s.seatnumber): s.userid is not None
        for s in session.seat_statuses
    }
    return templates.TemplateResponse(name='booking.html',
                                          context={'request': request,
                                                   'session': session,
                                                   "seat_statuses_map": seat_statuses_map,
                                                   'hall': hall})


@cinema_session_router.post('/booking/{sessionid}')
async def ticket_booking(
    sessionid: int,
    data: SeatBookingRequest,
    user: UserModel = Depends(get_current_user),
):
    success = await CinemaSessionService.book_seat(
        sessionid=sessionid,
        rownumber=data.rownumber,
        seatnumber=data.seatnumber,
        user=user
    )

    if not success:
        raise HTTPException(status_code=409, detail="Seat already booked")

    return {"status": "ok"}


@cinema_session_router.post("/booking/cancel/{sessionid}")
async def cancel_booking(
    sessionid: int,
    data: SeatBookingRequest,
    user=Depends(get_current_user)
):
    success = await CinemaSessionService.cancel_booking(
        sessionid=sessionid,
        rownumber=data.rownumber,
        seatnumber=data.seatnumber,
        userid=user.userid,
    )

    if not success:
        raise HTTPException(status_code=400, detail="Cannot cancel this booking")

    return {"message": "ok"}


@cinema_session_router.get('/success/{action}')
async def success_page(request: Request, action: str):
    return templates.TemplateResponse(name='success.html',
                                      context={'request': request,
                                               'action': action})
