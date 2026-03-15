from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

# from api.controllers_to_delete.cast_member_controller import cast_member_router
# from api.controllers_to_delete.cinema_session_controller import cinema_session_router
# from api.controllers_to_delete.country_controller import country_router
# from api.controllers_to_delete.hall_controller import hall_router
# from api.controllers_to_delete.movie_controller import movie_router
# from api.controllers_to_delete.user_controller import user_router


from api.routers.user_router import user_router
from api.routers.country_router import country_router
from api.routers.cast_member_router import cm_router
from api.routers.hall_router import hall_router
from api.routers.movie_router import movie_router
from api.routers.cinema_session_router import cs_router
from api.routers.page_router import page_router
from api.routers.registration_router import registration_router


import uvicorn

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory='templates')

app = FastAPI()

# app.include_router(cinema_session_router)
# app.include_router(user_router)
# app.include_router(movie_router)
# app.include_router(country_router)
# app.include_router(hall_router)
# app.include_router(cast_member_router)


app.include_router(user_router)
app.include_router(country_router)
app.include_router(cm_router)
app.include_router(hall_router)
app.include_router(movie_router)
app.include_router(cs_router)
app.include_router(page_router)
app.include_router(registration_router)


app.mount('/static', StaticFiles(directory='static'), 'static')


@app.get('/')
async def get(request: Request):
    return templates.TemplateResponse(name='home.html',
                                      context={'request': request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)