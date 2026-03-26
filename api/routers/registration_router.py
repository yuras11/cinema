from fastapi import APIRouter, HTTPException, status
from fastapi import Response
from api.comands.registration.login_command_handler import LoginCommandHandler
from api.comands.registration.register_user_command_handler import RegisterUserCommandHandler
from api.comands.registration.registration_commands import RegistrationCommand, LoginCommand
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from api.queries.user.get_user_by_login import GetUserByLoginQueryHandler
from config import get_auth_data
from fastapi.templating import Jinja2Templates


registration_router = APIRouter(prefix='/site', tags=['Site'])


@registration_router.post('/registration')
async def register_user(command: RegistrationCommand) -> dict:
    await RegisterUserCommandHandler.handle_async(command=command)
    return {'message': 'You have successfully signed in!'}


@registration_router.post('/login')
async def auth_user(response: Response, command: LoginCommand):
    access_token = await LoginCommandHandler.handle_async(command=command)
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token,
            'refresh_token': None,
            'message': 'User has logged in successfully'}


@registration_router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'User has logged out successfully'}
