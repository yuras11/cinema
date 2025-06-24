from fastapi import APIRouter, Depends

from dependencies import get_current_admin_user
from orm.user_model import UserModel
from pydantic_schemas.hall_schemas import HallScheme, HallNameScheme, SeatScheme, HallCreateScheme
from service.hall_service import HallService

hall_router = APIRouter(prefix='/halls', tags=["Working with halls"])

@hall_router.get('/all')
async def get_all_halls():
    halls = await HallService.get_all_halls()
    return [hall.model_dump() for hall in [HallScheme.model_validate(h) for h in halls]]


@hall_router.get('/hall_info')
async def get_hall_by_id(hallid):
    hall = await HallService.get_hall_by_id(hallid=hallid)
    return HallScheme.model_validate(hall)


@hall_router.post('/create_hall')
async def create_hall(hall_scheme: HallCreateScheme, user_data: UserModel = Depends(get_current_admin_user)):
    result = await HallService.create_hall(hall_scheme=hall_scheme)
    return {"message": 'Hall has been created'} if result else {'message': 'error'}


# @hall_router.put('/update_hall')
# async def update_hall(hall_scheme):
#     pass

@hall_router.delete('/delete_hall')
async def delete_hall(hallid, user_data: UserModel = Depends(get_current_admin_user)):
    result = await HallService.delete_hall(hallid=hallid)
    return {"message": 'Hall has been deleted'} if result else {'message': 'error'}