from repository.user_dao import UserRepository
from entity.user import User
from service.base_service import BaseService


class UserService(BaseService):
    def __init__(self, dao: UserRepository):
        super().__init__(dao)


    def get_user_by_initials(self, name, surname):
        return self._dao.find(name, surname)