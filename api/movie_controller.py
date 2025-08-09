import datetime
import uuid

from fastapi import APIRouter, Depends, Request
from typing import Optional, List

from dependencies import get_current_admin_user, get_current_user
from orm.user_model import UserModel
from pydantic_schemas.movie_schemas import MovieScheme, MovieNameScheme, MovieUpdateScheme
from service.movie_service import MovieService
from fastapi.templating import Jinja2Templates


movie_router = APIRouter(prefix='/movies', tags=['Working with movies'])
templates = Jinja2Templates(directory='templates')


@movie_router.get('/all', response_model=List[MovieScheme])
async def get_all_movies():
    movies = await MovieService.get_all_movies()
    return movies


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
async def get_movie_by_id(movieid: str,
                          request: Request,
                          user=Depends(get_current_user)):
    movie = await MovieService.get_movie_by_id(movieid=movieid)
    movie.cinema_sessions = list(filter(lambda x: x.sessiondate >= datetime.date.today(), movie.cinema_sessions))
    cinema_sessions_by_date = MovieService.get_cinema_sessions_by_date(movie=movie)
    return templates.TemplateResponse(name='movie.html',
                                      context={'request': request,
                                               'movie': movie,
                                               'user': user,
                                               'cinema_sessions_by_date': cinema_sessions_by_date})


@movie_router.post('/create_movie/')
async def create_movie(movie_scheme: MovieScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.create_movie(movie_scheme=movie_scheme)
    return {'message': f'Movie has been successfully created'} if result else {'message': 'Error'}


@movie_router.put('/update_movie/')
async def update_movie(movie_scheme: MovieUpdateScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.update_movie(movie_scheme=movie_scheme)
    return {'message': f'Movie has been successfully updated'} if result else {'message': 'Error'}


@movie_router.delete('/delete_movie')
async def delete_movie(movieid: uuid.UUID, user_data: UserModel = Depends(get_current_admin_user)):
    result = await MovieService.delete_movie(movieid=movieid)
    return {'message': f'Movie has been successfully deleted'} if result else {'message': 'Error'}