from dao.country_dao import CountryDAO
from entity.country import Country
from service.base_service import BaseService


class CountryService(BaseService):
    def __init__(self, dao: CountryDAO):
        super().__init__(dao)

