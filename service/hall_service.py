from repository.hall_dao import HallRepository
from entity.hall import Hall
from service.base_service import BaseService


class HallService(BaseService):
    def __init__(self, dao: HallRepository):
        super().__init__(dao)
