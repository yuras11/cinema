from dao.genre_dao import GenreDAO
from entity.genre import Genre
from service.base_service import BaseService


class GenreService(BaseService):
    def __init__(self, dao: GenreDAO):
        super().__init__(dao)
