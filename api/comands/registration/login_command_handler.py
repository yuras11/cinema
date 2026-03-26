from fastapi import HTTPException, status, Response
import datetime
from jose import jwt
from datetime import datetime, timedelta, timezone
from api.comands.registration.registration_commands import LoginCommand
from api.queries.user.get_user_by_login import GetUserByLoginQueryHandler
from passlib.context import CryptContext
from config import get_auth_data


class LoginCommandHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    async def handle_async(cls, command: LoginCommand):
        check = await cls.__authenticate_user(userlogin=command.userlogin, userpassword=command.userpassword)
        if check is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Wrong login or password')
        access_token = cls.__create_access_token({"sub": str(check.userid)})
        return access_token


    @classmethod
    async def __authenticate_user(cls, userlogin: str, userpassword: str):
        user = await GetUserByLoginQueryHandler.handle_async(userlogin=userlogin)
        user = user[0]
        if not user or cls.__verify_password(plain_password=userpassword, hashed_password=user.userpassword) is False:
            return None
        return user


    @classmethod
    def __verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)


    @classmethod
    def __create_access_token(cls, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=30)
        to_encode.update({"exp": expire})
        auth_data = get_auth_data()
        encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
        return encode_jwt