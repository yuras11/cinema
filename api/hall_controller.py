from fastapi import APIRouter, Depends

from dependencies import get_current_admin_user, get_current_user
from orm.user_model import UserModel
from pydantic_schemas.hall_schemas import SeatScheme, HallCreateScheme, HallUpdateScheme
from service.hall_service import HallService
from fastapi import Response, Request
from fastapi.templating import Jinja2Templates


hall_router = APIRouter(prefix='/halls', tags=["Working with halls"])
templates = Jinja2Templates(directory='templates')

@hall_router.get('/all')
async def get_all_halls():
    return await HallService.get_all()


@hall_router.get('/create')
async def create_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='hall/hall_creation.html',
                                      context={'request': request})


@hall_router.post('/create')
async def create_hall(hall_scheme: HallCreateScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await HallService.create_hall(hall_scheme=hall_scheme)
    return {"message": 'Hall has been created'} if result else {'message': 'error'}


@hall_router.get('/update')
async def update_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='hall/hall_update.html',
                                          context={'request': request})

@hall_router.put('/update')
async def update_hall(hall_scheme: HallUpdateScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await HallService.update_hall(hall_scheme=hall_scheme)
    return {"message": 'Hall has been updated'} if result else {'message': 'error'}


@hall_router.get('/delete')
async def delete_hall(request: Request,
                      is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                                          context={'request': request,
                                                   'entity': 'halls'})


@hall_router.delete('/delete')
async def delete_hall(hallid: int, user_data: UserModel = Depends(get_current_admin_user)):
    result = await HallService.delete_hall(hallid=hallid)
    return {"message": 'Hall has been deleted'} if result else {'message': 'error'}