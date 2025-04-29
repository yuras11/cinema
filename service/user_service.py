from repository.user_repository import UserRepository
from service.base_service import Service


class UserService(Service):
    def __init__(self):
        super().__init__()
        self._repository = UserRepository()


    def get_by_name(self, name):
        return self._repository.get_by_name(name)