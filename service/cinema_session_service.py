from repository.cinema_session_repo import CinemaSessionRepository
from service.base_service import Service
from sqlalchemy.orm import Session


class CinemaSessionService(Service):
    def __init__(self):
        super().__init__()
        self._repository = CinemaSessionRepository()


    def get_by_date(self, date):
        return self._repository.get_by_date(date)