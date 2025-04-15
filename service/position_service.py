from repository.position_repository import PositionRepository
from service.base_service import BaseService


class PositionService(BaseService):
    def __init__(self, repository: PositionRepository):
        super().__init__(repository)
