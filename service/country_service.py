from repository.country_dao import CountryRepository
from service.base_service import BaseService


class CountryService(BaseService):
    def __init__(self, dao: CountryRepository):
        super().__init__(dao)


    def get_by_name(self, name: str):
        return self._dao.get_by_name(name)
