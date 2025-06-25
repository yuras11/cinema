from repository.database import connection
from pydantic_schemas.movie_schemas import MovieScheme, MovieUpdateScheme
from repository.repos import MovieRepository
import uuid



class MovieService:
    @classmethod
    async def get_all_movies(cls):
        return await MovieRepository.get_all()


    @classmethod
    async def create_movie(cls, movie_scheme: MovieScheme):
        return await MovieRepository.insert(movie_scheme=movie_scheme)


    @classmethod
    async def update_movie(cls, movie_scheme: MovieUpdateScheme):
        return await MovieRepository.update(
            filters={'movieid': movie_scheme.movieid},
            values=movie_scheme.model_dump()
        )


    @classmethod
    async def delete_movie(cls, movieid: uuid.UUID):
        return await MovieRepository.delete(movieid=movieid)


# movies = asyncio.get_event_loop().run_until_complete(MovieService.get_all_movies())
# for movie in movies:
#     movie_p = MovieScheme.model_validate(movie)
#     print(movie_p.model_dump_json())