import uuid

from fastapi import APIRouter

from pydantic_schemas.cast_member_schemas import CastMemberScheme, CastMemberNameScheme, PositionScheme, PositionNameScheme, CastMemberCreateScheme
from service.cast_member_service import CastMemberService

cast_member_router = APIRouter(prefix='/cast_members', tags=["Working with cast members"])

@cast_member_router.get('/all')
async def get_all_cast_members():
    cast_members = await CastMemberService.get_all_cast_members()
    return [cast_member.model_dump() for cast_member in
            [CastMemberScheme.model_validate(c) for c in cast_members]]


@cast_member_router.post('/create_cast_member')
async def create_cast_member(cast_member_scheme: CastMemberCreateScheme):
    result = await CastMemberService.create_cast_member(cast_member_scheme=cast_member_scheme)
    if result:
        return 'OK'
    return 'ERROR'


@cast_member_router.put('/update_cast_member')
async def update_cast_member(cast_member_scheme: CastMemberScheme):
    pass


@cast_member_router.delete('/delete_cast_member')
async def delete_cast_member(memberid: uuid.UUID):
    result = await CastMemberService.delete_cast_member(memberid=memberid)
    return {'message': 'Cast member has been successfully deleted'} if result else {'message': 'Error'}