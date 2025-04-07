from dao.cast_member_dao import CastMemberDAO
from entity.cast_member import CastMember
from service.base_service import BaseService


class CastMemberService(BaseService):
    def __init__(self, dao: CastMemberDAO):
        super().__init__(dao)


    def get_by_movie(self, movie_id: str):
        return self._dao.get_by_movie(movie_id)