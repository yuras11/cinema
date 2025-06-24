from repository.database import connection
from pydantic_schemas.movie_schemas import MovieScheme
from repository.repos import MovieRepository
import asyncio


class MovieService:
    @classmethod
    async def get_all_movies(cls):
        return await MovieRepository.get_all()


    @classmethod
    async def create_movie(cls, movie_scheme: MovieScheme):
        return await MovieRepository.insert(movie_scheme=movie_scheme)


    @classmethod
    async def update_movie(cls, movie_scheme: MovieScheme):
        return await MovieRepository.update(movie_scheme=movie_scheme)


# movies = asyncio.get_event_loop().run_until_complete(MovieService.get_all_movies())
# for movie in movies:
#     movie_p = MovieScheme.model_validate(movie)
#     print(movie_p.model_dump_json())