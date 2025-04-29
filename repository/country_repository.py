from orm.country_model import CountryModel, CountryNameModel
from sqlalchemy import select
from repository.base_repository import Repository


class CountryRepository(Repository):
    def get_all(self):
        with self._session as session:
            statement = select(CountryModel)
            rows = [row for row in session.scalars(statement).all()]
            return rows


    def get_by_id(self, countrycode):
        with self._session as session:
            statement = select(CountryModel).where(CountryModel.countrycode == countrycode)
            country = session.scalars(statement).one()
            return country


    def get_by_name(name: str, session) -> CountryModel:
        statement = (
            select(CountryModel)
            .join(CountryNameModel)
            .where(CountryNameModel.countryname == name)
        )
        db_object = session.scalars(statement).one()
        return db_object