from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from dependencies import get_current_user, get_current_admin_user
from pydantic_schemas.cinema_session_schemas import CinemaSessionScheme
from service.cinema_session_service import CinemaSessionService


cinema_session_router = APIRouter(prefix='/cinema_sessions', tags=['Working with cinema sessions'])
templates = Jinja2Templates(directory='templates')

# @cinema_session_router.get('/all')
# async def get_all_cinema_sessions():
#     return await CinemaSessionService.get_all_cinema_sessions()


@cinema_session_router.get('/all')
async def get(request: Request,
              cinema_sessions=Depends(CinemaSessionService.get_all_cinema_sessions),
              user = Depends(get_current_user),
              is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='admin_toolpage.html',
                                          context={'request': request,
                                                   'user': user})
    return templates.TemplateResponse(name='cinema_sessions.html',
                                      context={'request': request,
                                               'cinema_sessions': cinema_sessions,
                                               'user': user})


@cinema_session_router.get('/today')
async def get_todays_billboard(request: Request,
              cinema_sessions=Depends(CinemaSessionService.get_todays_billboard),
              user = Depends(get_current_user),
              is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='admin_toolpage.html',
                                          context={'request': request,
                                                   'user': user})
    return templates.TemplateResponse(name='cinema_sessions.html',
                                      context={'request': request,
                                               'cinema_sessions': cinema_sessions,
                                               'user': user})


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
    return {'message': 'Cinema session has been successfully deleted'} if result else {'message': 'Error'}