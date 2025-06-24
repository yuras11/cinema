from repository.database import connection
from pydantic_schemas.hall_schemas import HallScheme, HallCreateScheme
from repository.repos import HallRepository
import asyncio


class HallService:
    @classmethod
    async def get_all_halls(cls):
        return await HallRepository.get_all()


    @classmethod
    async def get_hall_by_id(cls, hallid):
        return await HallRepository.get_by_primary_key(hallid=hallid)


    @classmethod
    async def create_hall(cls, hall_scheme: HallCreateScheme):
        return await HallRepository.insert(hall_scheme=hall_scheme)


    @classmethod
    async def delete_hall(cls, hallid):
        return await HallRepository.delete(hallid=hallid)

# halls = asyncio.get_event_loop().run_until_complete(HallService.get_all_halls())
# for hall in halls:
#     hall_p = HallScheme.model_validate(hall)
#     print(hall_p.model_dump_json())
