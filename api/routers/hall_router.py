from fastapi import APIRouter

from api.comands.hall.create_hall_command import CreateHallCommandHandler
from api.comands.hall.delete_hall_command import DeleteHallCommandHandler
from api.comands.hall.update_hall_command import UpdateHallCommandHandler
from api.queries.hall.get_all_halls_query import GetAllHallsQueryHandler
from api.queries.hall.get_hall_by_id_query import GetHallByIdQueryHandler
from pydantic_schemas.hall_schemas import HallCommand

test_hall_router = APIRouter(prefix='/test_halls', tags=["Halls"])

@test_hall_router.get('/')
async def get_all_halls():
    halls = await GetAllHallsQueryHandler.handle_async()
    return [h.to_dict() for h in halls]


@test_hall_router.get('/{hallid}')
async def get_hall_by_id(hallid: int):
    hall = await GetHallByIdQueryHandler.handle_async(hallid=hallid)
    return hall.to_dict()


@test_hall_router.post('/')
async def create_hall(command: HallCommand):
    result = await CreateHallCommandHandler.handle_async(command=command)
    return {'message': "Hall is successfully created"} if result else {'message': 'error'}


@test_hall_router.put('/{hallid}')
async def update_hall(hallid: int, command: HallCommand):
    result = await UpdateHallCommandHandler.handle_async(hallid=hallid, command=command)
    return {'message': "Hall is successfully updated"} if result else {'message': 'error'}


@test_hall_router.delete('/{hallid}')
async def delete_hall(hallid: int):
    result = await DeleteHallCommandHandler.handle_async(hallid=hallid)
    return {'message': "Hall is successfully deleted"} if result else {'message': 'error'}