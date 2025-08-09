import datetime
from cgitb import reset

from fastapi import APIRouter
from typing import List
from pydantic_schemas.user_schemas import UserScheme
from service.user_service import UserService

user_router = APIRouter(prefix='/cinema_users', tags=["Working with users"])

# @user_router.get('/{userlogin}')
# async def get_user_by_login(userlogin: str):
#     users = await UserService.get_user_by_login(userlogin=userlogin)
#     return users[0] if users else None


@user_router.get('/get_all_users')
async def get_all_users():
    users = await UserService.get_all_users()
    return users


@user_router.post('/add_user')
async def create_user(user: UserScheme):
    result = await UserService.create_user(**user.model_dump())
    if result:
        return f"User {user.userlogin} is successfully created"
    return "Failed to create user"


@user_router.put('/update_user')
async def update_user(user: UserScheme):
    result = await UserService.update_user(**user.model_dump())
    if result:
        return f"User {user.userlogin} is successfully updated"
    return "Failed to update user"


@user_router.delete('/delete_user')
async def delete_user(userid: str):
    result = await UserService.delete_user(userid=userid)
    if result:
        return {'message': "User is successfully deleted"}
    return "Failed to delete user"


