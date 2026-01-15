from fastapi import APIRouter, Request, UploadFile, Depends, HTTPException, status, Response
from fastapi.templating import Jinja2Templates
from api.user_controller import get_all_users, get_user_by_login
import shutil

from auth import get_password_hash, create_access_token
from pydantic_schemas.user_schemas import UserRegisterScheme, UserScheme, UserLoginScheme
from auth import authenticate_user
from service.user_service import UserService

router = APIRouter(tags=['Frontend'])
templates = Jinja2Templates(directory='templates')


# @router.get('/users')
# async def get_students_html(request: Request, users = Depends(get_all_users)):
#     return templates.TemplateResponse(name='users.html', context={'request': request, 'users': users})





# @router.get('/users/{userlogin}')
# async def get_user_html(request: Request, user=Depends(get_user_by_login)):
#     return templates.TemplateResponse(name='profile.html',
#                                       context={'request': request, 'user': user})
