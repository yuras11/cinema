import datetime

from orm.movie_model import MovieModel
from repository.database import connection
from pydantic_schemas.movie_schemas import MovieScheme, MovieUpdateScheme
from repository.repos import MovieRepository
import uuid



class MovieService:
    @classmethod
    async def get_all_movies(cls):
        return await MovieRepository.get_all()

    @classmethod
    async def get_movie_by_id(cls, movieid: int):
        return await MovieRepository.get_by_primary_key(movieid=movieid)


    @classmethod
    async def get_actual_movies(cls):
        """
        выбираем фильмы, на которые есть сеансы сегодня и в будущем.
        далее сеансы за прошлое нужно будет очищать.
        """
        movies = await MovieRepository.get_all()
        actual_movies = []
        for movie in movies:
            if movie.cinema_sessions:
                for cinema_session in movie.cinema_sessions:
                    if cinema_session.sessiondate >= datetime.date.today():
                        actual_movies.append(movie)
                        break
        return actual_movies


    @classmethod
    def get_cinema_sessions_by_date(cls, movie: MovieModel):
        cinema_sessions_by_date = dict()

        for cinema_session in filter(lambda x: x.sessiondate >= datetime.date.today(), movie.cinema_sessions):
            if cinema_session.sessiondate not in cinema_sessions_by_date.keys():
                cinema_sessions_by_date[cinema_session.sessiondate] = []
            cinema_sessions_by_date[cinema_session.sessiondate].append(cinema_session)

        return cinema_sessions_by_date


    @classmethod
    async def create_movie(cls, movie_scheme: MovieScheme):
        return await MovieRepository.create_movie(movie_scheme=movie_scheme)


    @classmethod
    async def update_movie(cls, movie_scheme: MovieUpdateScheme):
        return await MovieRepository.update_movie(movie_scheme=movie_scheme)


    @classmethod
    async def delete_movie(cls, movieid: int):
        return await MovieRepository.delete(movieid=movieid)


# movies = asyncio.get_event_loop().run_until_complete(MovieService.get_all_movies())
# for movie in movies:
#     movie_p = MovieScheme.model_validate(movie)
#     print(movie_p.model_dump_json())