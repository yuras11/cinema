from fastapi import APIRouter, HTTPException, status
from fastapi import Response
from api.comands.user.create_user_command import CreateUserCommandHandler
from auth import get_password_hash
from pydantic_schemas.user_schemas import UserCommand, UserLoginCommand
from auth import authenticate_user
from auth import create_access_token
from fastapi.templating import Jinja2Templates


registration_router = APIRouter(prefix='/site', tags=['Site'])
templates = Jinja2Templates(directory='templates')


@registration_router.post('/registration')
async def register_user(command: UserCommand) -> dict:
    await CreateUserCommandHandler.handle_async(command=command)
    return {'message': 'You have successfully signed in!'}


@registration_router.post('/login')
async def auth_user(response: Response, command: UserLoginCommand):
    check = await authenticate_user(userlogin=command.userlogin, userpassword=command.userpassword)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Wrong login or password')
    access_token = create_access_token({"sub": str(check.userid)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token,
            'refresh_token': None,
            'message': 'User has logged in successfully'}


@registration_router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'User has logged out successfully'}
