from fastapi import APIRouter

from api.comands.cast_member.create_cast_member_command import CreateCastMemberCommandHandler
from api.comands.cast_member.update_cast_member_command import UpdateCastMemberCommandHandler
from api.comands.cast_member.delete_cast_member_command import DeleteCastMemberCommandHandler
from api.queries.cast_member.get_all_cast_members_query import GetAllCastMembersQueryHandler
from api.queries.cast_member.get_cast_member_by_id_query import GetCastMemberByIdQueryHandler
from pydantic_schemas.cast_member_schemas import CastMemberCommand

cm_router = APIRouter(prefix='/cast_members', tags=["Cast_members"])


@cm_router.get('/')
async def get_all_cast_members():
    cast_members = await GetAllCastMembersQueryHandler.handle_async()
    return [cm.to_dict() for cm in cast_members]


@cm_router.get('/{memberid}')
async def get_cast_member_by_id(memberid: int):
    cast_member = await GetCastMemberByIdQueryHandler.handle_async(memberid=memberid)
    return cast_member.to_dict()


@cm_router.post('/')
async def create_cast_member(command: CastMemberCommand):
    result = await CreateCastMemberCommandHandler.handle_async(command=command)
    return {'message': "Cast member is successfully created"} if result else {'message': 'error'}


@cm_router.put('/{memberid}')
async def update_cast_member(memberid: int, command: CastMemberCommand):
    result = await UpdateCastMemberCommandHandler.handle_async(memberid=memberid, command=command)
    return {'message': "Cast member is successfully updated"} if result else {'message': 'error'}


@cm_router.delete('/{memberid}')
async def delete_cast_member(memberid: int):
    result = await DeleteCastMemberCommandHandler.handle_async(memberid=memberid)
    return {'message': "Cast member is successfully deleted"} if result else {'message': 'error'}