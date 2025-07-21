from fastapi import FastAPI

from api.cast_member_controller import cast_member_router
from api.cinema_session_controller import cinema_session_router
from api.country_controller import country_router
from api.hall_controller import hall_router
from api.movie_controller import movie_router
from api.user_controller import user_router
from pydantic_schemas.movie_schemas import MovieScheme
from registration_controller import registration_router
from repository.repos import MovieRepository
from service.movie_service import MovieService
import uvicorn

app = FastAPI()

app.include_router(cinema_session_router)
app.include_router(user_router)
app.include_router(movie_router)
app.include_router(country_router)
app.include_router(hall_router)
app.include_router(cast_member_router)
app.include_router(registration_router)


@app.get('/')
async def get():
    # movies = await MovieService.get_all_movies()
    # movies_p = [MovieScheme.model_validate(m) for m in movies]
    # return [movie.model_dump()["names"] for movie in movies_p]
    return 'hello'


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)