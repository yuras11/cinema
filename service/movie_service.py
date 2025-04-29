from entity.movie import Movie
from repository.movie_repo import MovieRepository
from service.base_service import Service
from sqlalchemy.orm import Session


class MovieService(Service):
    def __init__(self):
        super().__init__()
        self._repository = MovieRepository()


    def get_by_name(self, name):
        return self._repository.get_by_name(name)