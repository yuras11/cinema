from dao.hall_dao import HallDAO
from entity.hall import Hall
from service.base_service import BaseService


class HallService(BaseService):
    def __init__(self, dao: HallDAO):
        super().__init__(dao)
