from fastapi import APIRouter, HTTPException, status
from fastapi import Response
from api.comands.user.create_user_command import CreateUserCommandHandler
from api.comands.user.user_command import UserCommand, UserLoginCommand
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from api.queries.user.get_user_by_login import GetUserByLoginQueryHandler
from config import get_auth_data
from fastapi.templating import Jinja2Templates


registration_router = APIRouter(prefix='/site', tags=['Site'])
templates = Jinja2Templates(directory='templates')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


async def authenticate_user(userlogin: str, userpassword: str):
    user = await GetUserByLoginQueryHandler.handle_async(userlogin=userlogin)
    user = user[0]
    if not user or verify_password(plain_password=userpassword, hashed_password=user.userpassword) is False:
        return None
    return user


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
