from repository.database import connection
from pydantic_schemas.hall_schemas import HallCreateScheme, HallUpdateScheme
from repository.repos import HallRepository
import asyncio


class HallService:
    @classmethod
    async def get_all(cls):
        return await HallRepository.get_all()


    @classmethod
    async def get_hall_by_id(cls, hallid):
        return await HallRepository.get_by_primary_key(hallid=hallid)


    @classmethod
    async def create_hall(cls, hall_scheme: HallCreateScheme):
        return await HallRepository.create_hall(hall_scheme=hall_scheme)

    @classmethod
    async def update_hall(cls, hall_scheme: HallUpdateScheme):
        return await HallRepository.update_hall(hall_scheme=hall_scheme)

    @classmethod
    async def delete_hall(cls, hallid: int):
        return await HallRepository.delete(hallid=hallid)

