from fastapi import FastAPI
from api.cinema_session_controller import cinema_session_router
from repository.movie_repo import MovieRepository
from service.movie_service import MovieService
import uvicorn

app = FastAPI()

app.include_router(cinema_session_router)

@app.get('/')
def get():
    movie_service = MovieService()
    return [movie.names[0].moviename for movie in movie_service.get_all()]


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", reload=True)