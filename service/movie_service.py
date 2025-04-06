from dao.movie_dao import MovieDAO
from entity.movie import Movie
from service.base_service import BaseService


class MovieService(BaseService):
    def __init__(self, dao: MovieDAO):
        super().__init__(dao)


    def get_by_country(self, country_code):
        return self._dao.get_by_country(country_code)