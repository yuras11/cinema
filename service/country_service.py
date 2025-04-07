from dao.country_dao import CountryDAO
from service.base_service import BaseService


class CountryService(BaseService):
    def __init__(self, dao: CountryDAO):
        super().__init__(dao)


    def get_by_name(self, name: str):
        return self._dao.get_by_name(name)
