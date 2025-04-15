from repository.cinema_session_dao import CinemaSessionRepository
from service.base_service import BaseService


class CinemaSessionService(BaseService):
    def __init__(self, dao: CinemaSessionRepository):
        super().__init__(dao)


    def get_by_movie_from_date_to_date(self, movie_id: str, start_date: str, end_date: str):
        return self._dao.get_by_movie_from_date_to_date(movie_id, start_date, end_date)


    def get_by_dates(self, start_date: str, end_date: str):
        return self._dao.get_by_dates(start_date, end_date)


    def get_by_date(self, date):
        return self.get_by_dates(date, date)

