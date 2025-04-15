from repository.hall_repository import HallRepository
from entity.hall import Hall
from service.base_service import BaseService


class HallService(BaseService):
    def __init__(self, repository: HallRepository):
        super().__init__(repository)
