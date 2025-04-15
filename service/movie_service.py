from repository.movie_repository import MovieRepository
from service.base_service import BaseService


class MovieService(BaseService):
    def __init__(self, repository: MovieRepository):
        super().__init__(repository)


    def get_by_country(self, country_code):
        return self._repository.get_by_country(country_code)


    def get_by_cast_member(self, member_id: str):
        return self._repository.get_by_cast_member(member_id)