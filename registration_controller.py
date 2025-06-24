from fastapi import APIRouter, HTTPException, status, Depends
from fastapi import Response
from auth import get_password_hash
from orm.user_model import UserModel
from service.user_service import UserService
from pydantic_schemas.user_schemas import UserScheme
from auth import authenticate_user
from auth import create_access_token
from dependencies import get_current_user, get_current_admin_user


registration_router = APIRouter(prefix='/auth', tags=['Auth'])


@registration_router.post("/register/")
async def register_user(user_data: UserScheme) -> dict:
    user = await UserService.get_user_by_login(userlogin=user_data.userlogin)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['userpassword'] = get_password_hash(user_data.userpassword)
    await UserService.create_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@registration_router.post("/login/")
async def auth_user(response: Response, user_data: UserScheme):
    check = await authenticate_user(userlogin=user_data.userlogin, userpassword=user_data.userpassword)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверный логин или пароль')
    access_token = create_access_token({"sub": str(check.userid)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@registration_router.get("/me/")
async def get_me(user_data: UserModel = Depends(get_current_user)):
    return UserScheme.model_validate(user_data)


@registration_router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@registration_router.get("/all_users/")
async def get_all_users(user_data: UserModel = Depends(get_current_admin_user)):
    return await UserService.get_all_users()