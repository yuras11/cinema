from repository.genre_dao import GenreRepository
from entity.genre import Genre
from service.base_service import BaseService


class GenreService(BaseService):
    def __init__(self, dao: GenreRepository):
        super().__init__(dao)
