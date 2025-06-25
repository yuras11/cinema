import datetime
import uuid

from fastapi import APIRouter, Depends
from typing import Optional, List

from dependencies import get_current_admin_user
from orm.user_model import UserModel
from pydantic_schemas.movie_schemas import MovieScheme, MovieNameScheme, MovieUpdateScheme
from service.movie_service import MovieService


movie_router = APIRouter(prefix='/movies', tags=['Working with movies'])

@movie_router.get('/all', response_model=List[MovieScheme])
async def get_all_movies():
    movies = await MovieService.get_all_movies()
    return [m.model_dump() for m in [MovieScheme.model_validate(c) for c in movies]]


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