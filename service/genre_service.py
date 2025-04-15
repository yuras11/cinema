from repository.genre_repository import GenreRepository
from entity.genre import Genre
from service.base_service import BaseService


class GenreService(BaseService):
    def __init__(self, repository: GenreRepository):
        super().__init__(repository)
