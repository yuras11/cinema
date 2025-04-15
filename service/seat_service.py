from repository.seat_dao import SeatRepository
from entity.seat import Seat
from service.base_service import BaseService


class SeatService(BaseService):
    def __init__(self, dao: SeatRepository):
        super().__init__(dao)


    def get_by_hall_occupation(self, hall_id: str, is_occupied: bool):
        self._dao.get_by_hall_occupation(hall_id, is_occupied)