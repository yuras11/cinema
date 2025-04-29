from orm.cinema_session_model import CinemaSessionModel
from sqlalchemy import select
from repository.base_repository import Repository


class CinemaSessionRepository(Repository):
    def get_all(self):
        with self._session as session:
            statement = select(CinemaSessionModel)
            rows = [row for row in session.scalars(statement).all()]
            return rows


    def get_by_id(self, movieid, hallid, sessiondate, sessiontime):
        with self._session as session:
            statement = (
                select(CinemaSessionModel)
                .where(CinemaSessionModel.movieid == movieid)
                .where(CinemaSessionModel.hallid == hallid)
                .where(CinemaSessionModel.sessiondate == sessiondate)
                .where(CinemaSessionModel.sessiontime == sessiontime)
            )
            cinema_session = session.scalars(statement).one()
            return cinema_session


    def get_by_date(self, date):
        with self._session as session:
            statement = select(CinemaSessionModel).where(CinemaSessionModel.sessiondate == date)
            rows = [row for row in session.scalars(statement).all()]
            return rows