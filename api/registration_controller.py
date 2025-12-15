from fastapi import APIRouter, HTTPException, status, Depends
from fastapi import Response, Request
from auth import get_password_hash
from orm.user_model import UserModel
from service.user_service import UserService
from pydantic_schemas.user_schemas import UserRegisterScheme, UserLoginScheme
from auth import authenticate_user
from auth import create_access_token
from dependencies import get_current_user, get_current_admin_user
from fastapi.templating import Jinja2Templates


registration_router = APIRouter(prefix='/auth', tags=['Auth'])
templates = Jinja2Templates(directory='templates')


# registration
@registration_router.get('/registration')
async def register_form(request: Request):
    return templates.TemplateResponse(name="registration.html",
                                      context={"request": request})


@registration_router.post('/registration')
async def register_user(user_data: UserRegisterScheme) -> dict:
    user_dict = user_data.model_dump()
    user_dict['userpassword'] = get_password_hash(user_data.userpassword)
    await UserService.create_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


# login
@registration_router.get('/login')
async def auth_form(request: Request):
    return templates.TemplateResponse(name='login.html',
                                      context={'request': request})


@registration_router.post("/login")
async def auth_user(response: Response, user_data: UserLoginScheme):
    check = await authenticate_user(userlogin=user_data.userlogin, userpassword=user_data.userpassword)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверный логин или пароль')
    access_token = create_access_token({"sub": str(check.userid)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token,
            'refresh_token': None,
            'message': 'User has logged in successfully'}


@registration_router.get("/profile")
async def get_user_profile(request: Request,
                           user=Depends(get_current_user),
                           is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='admin_toolpage.html',
                                          context={'request': request,
                                                   'user': is_admin})
    return templates.TemplateResponse(name='profile.html',
                                      context={'request': request,
                                               'user': user})


@registration_router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}
