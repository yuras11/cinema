from repository.cast_member_repository import CastMemberRepository
from entity.cast_member import CastMember
from service.base_service import BaseService


class CastMemberService(BaseService):
    def __init__(self, repository: CastMemberRepository):
        super().__init__(repository)


    def get_by_movie(self, movie_id: str):
        return self._repository.get_by_movie(movie_id)