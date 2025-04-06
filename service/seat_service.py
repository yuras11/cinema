from dao.seat_dao import SeatDAO
from entity.seat import Seat
from service.base_service import BaseService


class SeatService(BaseService):
    def __init__(self, dao):
        super().__init__(dao)
