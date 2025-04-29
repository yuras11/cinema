from repository.cast_member_repo import CastMemberRepository
from service.base_service import Service


class CastMemberService(Service):
    def __init__(self):
        super().__init__()
        self._repository = CastMemberRepository()


    def get_by_name(self, name: str):
        return self._repository.get_by_name(name)