from fastapi import APIRouter, HTTPException, status, Depends, Request, Response
from fastapi.templating import Jinja2Templates
from dependencies import get_current_admin_user


page_router = APIRouter(prefix='/pages', tags=['HTML pages'])
templates = Jinja2Templates(directory='templates')


@page_router.get('/users/create')
async def create_user(request: Request, is_admin = Depends(get_current_admin_user)):
    if is_admin:
        return templates.TemplateResponse(name='user/user_creation.html',
                                          context={'request': request})


