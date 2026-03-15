from fastapi import APIRouter

from api.comands.user.create_user_command import CreateUserCommandHandler
from api.comands.user.update_user_command import UpdateUserCommandHandler
from api.queries.user.get_all_users_query import GetAllUsersQueryHandler
from api.queries.user.get_user_by_id_query import GetUserByIdQueryHandler
from service.user_service import UserService
from pydantic_schemas.user_schemas import UserCommand

user_router = APIRouter(prefix='/users', tags=["Users"])

@user_router.get('/')
async def get_all_users():
    users = await GetAllUsersQueryHandler.handle_async()
    return [user.to_dict() for user in users]


@user_router.get('/{userid}')
async def get_all_users(userid: str):
    user = await GetUserByIdQueryHandler.handle_async(userid=userid)
    return user.to_dict()


@user_router.post('/')
async def create_user(user: UserCommand):
    result = await CreateUserCommandHandler.handle_async(command=user)
    return {'message': "User is successfully created"} if result else {'message': 'error'}


@user_router.put('/{userid}')
async def update_user(userid: str, user: UserCommand):
    result = await UpdateUserCommandHandler.handle_async(userid=userid, command=user)
    return {'message': "User is successfully updated"} if result else {'message': 'error'}


@user_router.delete('/{userid}')
async def delete_user(userid: str):
    result = await UserService.delete_user(userid=userid)
    return {'message': "User is successfully deleted"} if result else {'message': 'error'}


# @user_router.post('/add_photo')
# async def add_student_photo(file: UploadFile, image_name: int):
#     with open(f"static/images/{image_name}.webp", "wb+") as photo_obj:
#         shutil.copyfileobj(file.file, photo_obj)
