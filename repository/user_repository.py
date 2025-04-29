from orm.user_model import UserModel
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from repository.base_repository import Repository


class UserRepository(Repository):
    def get_all(self):
        with self._session as session:
            statement = select(UserModel)
            rows = [row for row in session.scalars(statement).all()]
            return rows


    def get_by_id(self, userid):
        with self._session as session:
            statement = select(UserModel).where(UserModel.userid == userid)
            user = session.scalars(statement).one()
            return user


    def get_by_name(self, name):
        with self._session as session:
            statement = select(UserModel).where(UserModel.username == name)
            rows = [row for row in session.scalars(statement).all()]
            return rows
