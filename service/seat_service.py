from repository.seat_repository import SeatRepository
from entity.seat import Seat
from service.base_service import BaseService


class SeatService(BaseService):
    def __init__(self, repository: SeatRepository):
        super().__init__(repository)


    def get_by_hall_occupation(self, hall_id: str, is_occupied: bool):
        self._repository.get_by_hall_occupation(hall_id, is_occupied)