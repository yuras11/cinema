from repository.database import connection
from pydantic_schemas.cast_member_schemas import CastMemberCreateScheme, CastMemberUpdateScheme
from repository.repos import CastMemberRepository
import asyncio
import uuid


class CastMemberService:
    @classmethod
    async def get_all_cast_members(cls):
        return await CastMemberRepository.get_all()


    @classmethod
    async def create_cast_member(cls, cast_member_scheme: CastMemberCreateScheme):
        return await CastMemberRepository.insert(**cast_member_scheme.model_dump())


    @classmethod
    async def update_cast_member(cls, cast_member_scheme: CastMemberUpdateScheme):
        return await CastMemberRepository.update(
            filters={'memberid': cast_member_scheme.memberid},
            values=cast_member_scheme.model_dump()
        )


    @classmethod
    async def delete_cast_member(cls, memberid: int):
        return await CastMemberRepository.delete(memberid=memberid)


# cast_members = asyncio.get_event_loop().run_until_complete(CastMemberService.get_all_cast_members())
# for cast_member in cast_members:
#     cast_member_p = CastMemberScheme.model_validate(cast_member)
#     print(cast_member_p.model_dump_json())