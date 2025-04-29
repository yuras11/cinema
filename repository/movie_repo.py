from orm.movie_model import MovieModel, MovieNameModel
from sqlalchemy import select
from repository.base_repository import Repository


class MovieRepository(Repository):
    def get_all(self):
        with self._session as session:
            statement = select(MovieModel)
            rows = [row for row in session.scalars(statement).all()]
            return rows


    def get_by_id(self, movieid):
        with self._session as session:
            statement = select(MovieModel).where(MovieModel.movieid == movieid)
            movie = session.scalars(statement).one()
            return movie


    def get_by_name(self, name: str):
        with self._session as session:
            statement = (
                select(MovieModel)
                .join(MovieNameModel)
                .where(MovieNameModel.moviename == name)
            )
            movie = session.scalars(statement).one()
            return movie