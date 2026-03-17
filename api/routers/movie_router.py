from fastapi import APIRouter

from api.comands.movie.create_movie_command import CreateMovieCommandHandler
from api.comands.movie.delete_movie_command import DeleteMovieCommandHandler
from api.comands.movie.update_movie_command import UpdateMovieCommandHandler
from api.queries.movie.get_all_movies_query import GetAllMoviesQueryHandler
from api.queries.movie.get_movie_by_id_query import GetMovieByIdQueryHandler
from api.comands.movie.movie_command import MovieCommand

movie_router = APIRouter(prefix='/movies', tags=["Movies"])

@movie_router.get('/')
async def get_all_movies():
    movies = await GetAllMoviesQueryHandler.handle_async()
    return [m.to_dict() for m in movies]


@movie_router.get('/{movieid}')
async def get_movie_by_id(movieid: int):
    movie = await GetMovieByIdQueryHandler.handle_async(movieid=movieid)
    return movie.to_dict()


@movie_router.post('/')
async def create_movie(command: MovieCommand):
    result = await CreateMovieCommandHandler.handle_async(command=command)
    return {'message': "Movie is successfully created"} if result else {'message': 'error'}


@movie_router.put('/{movieid}')
async def update_movie(movieid: int, command: MovieCommand):
    result = await UpdateMovieCommandHandler.handle_async(movieid=movieid, command=command)
    return {'message': "Movie is successfully updated"} if result else {'message': 'error'}


@movie_router.delete('/{movieid}')
async def delete_movie(movieid: int):
    result = await DeleteMovieCommandHandler.handle_async(movieid=movieid)
    return {'message': "Movie is successfully deleted"} if result else {'message': 'error'}