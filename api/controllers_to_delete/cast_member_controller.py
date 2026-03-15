from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from dependencies import get_current_admin_user
from pydantic_schemas.cast_member_schemas import CastMemberCreateScheme, CastMemberUpdateScheme
from service.cast_member_service import CastMemberService

cast_member_router = APIRouter(prefix='/cast_members', tags=["Working with cast members"])
templates = Jinja2Templates(directory='templates')

@cast_member_router.get('/all')
async def get_all_cast_members():
    cast_members = await CastMemberService.get_all_cast_members()
    return [cast_member.model_dump() for cast_member in
            [CastMemberUpdateScheme.model_validate(c) for c in cast_members]]


@cast_member_router.get('/create')
async def create_cast_member(request: Request,
                             is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cast_member/cast_creation.html',
                                          context={'request': request})


@cast_member_router.post('/create')
async def create_cast_member(cast_member_scheme: CastMemberCreateScheme):
    result = await CastMemberService.create_cast_member(cast_member_scheme=cast_member_scheme)
    return {'message': 'Cast member has been successfully created'} if result else {'message': 'Error'}


@cast_member_router.get('/update')
async def update_cast_member(request: Request,
                             is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='cast_member/cast_update.html',
                                          context={'request': request})


@cast_member_router.put('/update')
async def update_cast_member(cast_member_scheme: CastMemberUpdateScheme):
    result = await CastMemberService.update_cast_member(cast_member_scheme=cast_member_scheme)
    return {'message': 'Cast member has been successfully updated'} if result else {'message': 'Error'}


@cast_member_router.get('/delete')
async def delete_cast_member(request: Request,
                             is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                          context={'request': request,
                                                   'entity': 'cast_members'})


@cast_member_router.delete('/delete')
async def delete_cast_member(cast_memberid: int):
    result = await CastMemberService.delete_cast_member(memberid=cast_memberid)
    return {'message': 'Cast member has been successfully deleted'} if result else {'message': 'Error'}