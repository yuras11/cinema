from repository.country_repository import CountryRepository
from service.base_service import BaseService


class CountryService(BaseService):
    def __init__(self, repository: CountryRepository):
        super().__init__(repository)


    def get_by_name(self, name: str):
        return self._repository.get_by_name(name)
