from fastapi import APIRouter, HTTPException, status, Depends, Request, Response
from fastapi.templating import Jinja2Templates
import datetime

from api.queries.cinema_session.get_cinema_session_by_id_query import GetCinemaSessionByIdQueryHandler
from api.queries.hall.get_hall_by_id_query import GetHallByIdQueryHandler
from api.queries.movie.get_actual_movies_query import GetActualMoviesQueryHandler
from api.queries.movie.get_movie_by_id_query import GetMovieByIdQueryHandler
from dependencies import get_current_admin_user, get_current_user, get_actual_movies

page_router = APIRouter(prefix='/pages', tags=['HTML pages'])
templates = Jinja2Templates(directory='templates')


@page_router.get('/users/create')
async def create_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='user/user_creation.html',
                                          context={'request': request})


@page_router.get('/users/update')
async def update_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='user/user_update.html',
                               context={'request': request})


@page_router.get('/users/delete')
async def delete_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                               context={'request': request,
                                        'entity': 'users'})


@page_router.get('/movies/create')
async def create_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='movie/movie_creation.html',
                                      context={'request': request})


@page_router.get('/movies/update')
async def update_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='movie/movie_update.html',
                                      context={'request': request})


@page_router.get('/movies/delete')
async def delete_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                      context={'request': request,
                                               'entity': 'movies'})


@page_router.get('/movies/{movieid}')
async def get_movie_by_id(movieid: int,
                          request: Request,
                          user=Depends(get_current_user)):
    movie = await GetMovieByIdQueryHandler.handle_async(movieid=movieid)
    movie.cinema_sessions = list(filter(lambda x: x.sessiondate >= datetime.date.today(), movie.cinema_sessions))

    cinema_sessions_by_date = dict()
    for cinema_session in filter(lambda x: x.sessiondate >= datetime.date.today(), movie.cinema_sessions):
        if cinema_session.sessiondate not in cinema_sessions_by_date.keys():
            cinema_sessions_by_date[cinema_session.sessiondate] = []
        cinema_sessions_by_date[cinema_session.sessiondate].append(cinema_session)

    director = list(filter(lambda x: x.professionid == 2, movie.cast_members))[0]
    cast = list(filter(lambda x: x.professionid == 1, movie.cast_members))
    return templates.TemplateResponse(name='movie/movie.html',
                                      context={'request': request,
                                               'movie': movie,
                                               'user': user,
                                               'cinema_sessions_by_date': cinema_sessions_by_date,
                                               'director': director,
                                               'cast': cast})


@page_router.get('/movies/all/actual')
async def get_actual_movies(request: Request,
              actual_movies=Depends(get_actual_movies),
              user = Depends(get_current_user)):
    """
    Получение всех фильмов, сеансы по которым есть сегодня и в будущем.
    """
    c = actual_movies
    return templates.TemplateResponse(name='actual_movie_list.html',
                                      context={'request': request,
                                               'movies': actual_movies,
                                               'user': user})


@page_router.get('/halls/create')
async def create_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='hall/hall_creation.html',
                                      context={'request': request})


@page_router.get('/halls/update')
async def update_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='hall/hall_update.html',
                                          context={'request': request})


@page_router.get('/halls/delete')
async def delete_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                          context={'request': request,
                                                   'entity': 'halls'})


@page_router.get('/cinema_sessions/create')
async def create_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cinema_session/session_creation.html',
                                          context={'request': request})


@page_router.get('/cinema_sessions/update')
async def update_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cinema_session/session_update.html',
                                          context={'request': request})


@page_router.get('/cinema_sessions/delete')
async def update_cinema_session(request: Request,
                                is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                          context={'request': request,
                                                   'entity': 'cinema_sessions'})


@page_router.get('/cinema_sessions/booking/{sessionid}')
async def ticket_booking(sessionid: int,
                         request: Request):
    session = await GetCinemaSessionByIdQueryHandler.handle_async(sessionid=sessionid)
    hall = await GetHallByIdQueryHandler.handle_async(hallid=session.hallid)
    seat_statuses_map = {
        (s.rownumber, s.seatnumber): s.userid is not None
        for s in session.seat_statuses
    }
    return templates.TemplateResponse(name='booking.html',
                                          context={'request': request,
                                                   'session': session,
                                                   "seat_statuses_map": seat_statuses_map,
                                                   'hall': hall})


@page_router.get('/success/{action}')
async def success_page(request: Request, action: str):
    return templates.TemplateResponse(name='success.html',
                                      context={'request': request,
                                               'action': action})


@page_router.get('/site/registration')
async def register_form(request: Request):
    return templates.TemplateResponse(name="registration.html",
                                      context={"request": request})


@page_router.get('/site/login')
async def auth_form(request: Request):
    return templates.TemplateResponse(name='login.html',
                                      context={'request': request})


@page_router.get('/site/profile')
async def get_user_profile(request: Request,
                           user=Depends(get_current_user),
                           is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='admin_toolpage.html',
                                          context={'request': request,
                                                   'user': is_admin})
    return templates.TemplateResponse(name='profile.html',
                                      context={'request': request,
                                               'user': user})