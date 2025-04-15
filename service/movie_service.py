from repository.movie_dao import MovieRepository
from service.base_service import BaseService


class MovieService(BaseService):
    def __init__(self, dao: MovieRepository):
        super().__init__(dao)


    def get_by_country(self, country_code):
        return self._dao.get_by_country(country_code)


    def get_by_cast_member(self, member_id: str):
        return self._dao.get_by_cast_member(member_id)