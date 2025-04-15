from repository.user_repository import UserRepository
from entity.user import User
from service.base_service import BaseService


class UserService(BaseService):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)


    def get_user_by_initials(self, name, surname):
        return self._repository.find(name, surname)