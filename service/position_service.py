from repository.position_dao import PositionRepository
from service.base_service import BaseService


class PositionService(BaseService):
    def __init__(self, dao: PositionRepository):
        super().__init__(dao)
