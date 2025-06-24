import datetime
from cgitb import reset

from fastapi import APIRouter
from typing import List
from pydantic_schemas.user_schemas import UserScheme
from service.user_service import UserService

user_router = APIRouter(prefix='/users', tags=["Working with users"])

@user_router.get('/user_by_login', response_model=List[UserScheme])
async def get_user_by_login(userlogin: str):
    users = await UserService.get_user_by_login(login=userlogin)
    users_p = [UserScheme.model_validate(u) for u in users]
    return [u_p.model_dump() for u_p in users_p]


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
async def delete_user(user: UserScheme):
    result = await UserService.delete_user(userid=user.userid)
    if result:
        return f"User {user.userlogin} is successfully deleted"
    return "Failed to delete user"


