import datetime
import uuid

from fastapi import APIRouter, Depends, Request
from typing import Optional, List

from dependencies import get_current_admin_user, get_current_user
from orm.user_model import UserModel
from pydantic_schemas.movie_schemas import MovieScheme, MovieUpdateScheme, MovieGetAllScheme
from service.movie_service import MovieService
from fastapi.templating import Jinja2Templates


movie_router = APIRouter(prefix='/movies', tags=['Working with movies'])
templates = Jinja2Templates(directory='templates')


@movie_router.get('/all')
async def get_all_movies():
    movies = await MovieService.get_all_movies()
    return [movie.model_dump() for movie in
            [MovieGetAllScheme.model_validate(c) for c in movies]]


@movie_router.get('/actual')
async def get_actual_movies(request: Request,
              actual_movies=Depends(MovieService.get_actual_movies),
              user = Depends(get_current_user)):
    """
    Получение всех фильмов, сеансы по которым есть сегодня и в будущем.
    """
    return templates.TemplateResponse(name='actual_movie_list.html',
                                      context={'request': request,
                                               'movies': actual_movies,
                                               'user': user})


@movie_router.get('/all/{movieid}')
async def get_movie_by_id(movieid: int,
                          request: Request,
                          user=Depends(get_current_user)):
    movie = await MovieService.get_movie_by_id(movieid=movieid)
    movie.cinema_sessions = list(filter(lambda x: x.sessiondate >= datetime.date.today(), movie.cinema_sessions))
    cinema_sessions_by_date = MovieService.get_cinema_sessions_by_date(movie=movie)
    director = list(filter(lambda x: x.professionid == 2, movie.cast_members))[0]
    cast = list(filter(lambda x: x.professionid == 1, movie.cast_members))
    return templates.TemplateResponse(name='movie/movie.html',
                                      context={'request': request,
                                               'movie': movie,
                                               'user': user,
                                               'cinema_sessions_by_date': cinema_sessions_by_date,
                                               'director': director,
                                               'cast': cast})


@movie_router.get('/create')
async def create_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='movie/movie_creation.html',
                                      context={'request': request})


@movie_router.post('/create')
async def create_movie(movie_scheme: MovieScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.create_movie(movie_scheme=movie_scheme)
    return {'message': f'Movie has been successfully created'} if result else {'message': 'Error'}


@movie_router.get('/update')
async def update_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='movie/movie_update.html',
                                      context={'request': request})


@movie_router.put('/update')
async def update_movie(movie_scheme: MovieUpdateScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.update_movie(movie_scheme=movie_scheme)
    return {'message': f'Movie has been successfully updated'} if result else {'message': 'Error'}


@movie_router.get('/delete')
async def delete_movie(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                      context={'request': request,
                                               'entity': 'movies'
                                               })


@movie_router.delete('/delete')
async def delete_movie(movieid: int, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.delete_movie(movieid=movieid)
    return {'message': f'Movie has been successfully deleted'} if result else {'message': 'Error'}