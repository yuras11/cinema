from repository.repos import UserRepository
from pydantic_schemas.user_schemas import UserUpdateScheme
from uuid import UUID


class UserService:
    @classmethod
    async def get_all_users(cls):
        return await UserRepository.get_all()


    @classmethod
    async def get_user_by_name(cls, name: str):
        return await UserRepository.find(username=name)


    @classmethod
    async def get_user_by_id(cls, userid: UUID):
        return await UserRepository.find(userid=userid)


    @classmethod
    async def get_user_by_login(cls, userlogin: str):
        return await UserRepository.find(userlogin=userlogin)


    @classmethod
    async def create_user(cls, **user_data):
        return await UserRepository.insert(**user_data)


    @classmethod
    async def update_user(cls, user_scheme: UserUpdateScheme):
        user_data = user_scheme.model_dump()
        filters = {'userid':user_data['userid']}
        values = {key: value for key, value in user_data.items() if key != 'userid'}
        return await UserRepository.update(filters=filters, values=values)


    @classmethod
    async def delete_user(cls, userid):
        return await UserRepository.delete(userid=userid)


# users = asyncio.get_event_loop().run_until_complete(UserService.get_all_users())
# for u in users:
#     u_p = UserScheme.model_validate(u)
#     print(u_p.model_dump_json())