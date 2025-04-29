from repository.country_repository import CountryRepository
from service.base_service import Service


class CountryService(Service):
    def __init__(self):
        super().__init__()
        self._repository = CountryRepository()


    def get_by_name(self, name: str):
        return self._repository.get_by_name(name)
