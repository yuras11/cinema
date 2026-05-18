from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
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
from exceptions.exception_handlers import register_exception_handlers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager
from jobs.ticket_cleanup_job import DeleteExpiredTicketsJob

templates = Jinja2Templates(directory='templates')
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    scheduler.add_job(
        DeleteExpiredTicketsJob.handle_async,
        trigger="cron",
        hour=12,
        minute=0
    )

    scheduler.start()

    print("Scheduler started")

    yield

    # shutdown
    scheduler.shutdown()

    print("Scheduler stopped")


app = FastAPI(lifespan=lifespan)

register_exception_handlers(app)

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
    return templates.TemplateResponse('home.html',
                                      {'request': request})




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)