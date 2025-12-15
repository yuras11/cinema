from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from dependencies import get_current_user, get_current_admin_user
from pydantic_schemas.cinema_session_schemas import CinemaSessionCreateScheme, CinemaSessionUpdateScheme
from service.cinema_session_service import CinemaSessionService


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