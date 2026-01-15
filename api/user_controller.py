from fastapi import APIRouter, Request, UploadFile
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from dependencies import get_current_admin_user
from service.user_service import UserService
from pydantic_schemas.user_schemas import UserRegisterScheme, UserUpdateScheme
import shutil

user_router = APIRouter(prefix='/users', tags=["Working with users"])
templates = Jinja2Templates(directory='templates')

@user_router.get('/all')
async def get_all_users():
    users = await UserService.get_all_users()
    return users


@user_router.get('/create')
async def create_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='user/user_creation.html',
                               context={'request': request})


@user_router.post('/create')
async def create_user(user: UserRegisterScheme):
    result = await UserService.create_user(**user.model_dump())
    return {'message': "User is successfully created"} if result else {'message': 'error'}


@user_router.get('/update')
async def update_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='user/user_update.html',
                               context={'request': request})


@user_router.put('/update')
async def update_user(user: UserUpdateScheme):
    result = await UserService.update_user(user_scheme=user)
    return {'message': "User is successfully updated"} if result else {'message': 'error'}


@user_router.get('/delete')
async def delete_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='entity_delete.html',
                               context={'request': request,
                                        'entity': 'users'})


@user_router.delete('/delete')
async def delete_user(userid: str):
    result = await UserService.delete_user(userid=userid)
    return {'message': "User is successfully deleted"} if result else {'message': 'error'}


# @user_router.post('/add_photo')
# async def add_student_photo(file: UploadFile, image_name: int):
#     with open(f"static/images/{image_name}.webp", "wb+") as photo_obj:
#         shutil.copyfileobj(file.file, photo_obj)
