from repository.hall_repository import HallRepository
from sqlalchemy.orm import Session
from service.base_service import Service


class HallService(Service):
    def __init__(self):
        super().__init__()
        self._repository = HallRepository()


    def get_by_name(self, name):
        return self._repository.get_by_name(name)
