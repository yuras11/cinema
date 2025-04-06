from dao.position_dao import PositionDAO
from entity.position import Position
from service.base_service import BaseService


class PositionService(BaseService):
    def __init__(self, dao: PositionDAO):
        super().__init__(dao)
