import psycopg2
import uuid

from dao.cast_member_dao import CastMemberDAO
from dao.cinema_session_dao import CinemaSessionDAO
from dao.country_dao import CountryDAO
from dao.genre_dao import GenreDAO
from dao.hall_dao import HallDAO
from dao.movie_dao import MovieDAO
from dao.position_dao import PositionDAO
from dao.seat_dao import SeatDAO
from dao.user_dao import UserDAO
from entity.cast_member import CastMember
from service.cinema_session_service import CinemaSessionService
from service.country_service import CountryService
from service.movie_service import MovieService

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "cinema"
DB_USER = "postgres"
DB_PASSWORD = "12345678"


connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


cinema = CinemaSessionService(CinemaSessionDAO(connection))
m = cinema.get("69dd5174-4c78-4d0f-a6e8-b24482af20a9", "108fb5a2-c524-4fc2-9789-7b7a6ee93c5f", "2025-03-21", "20:30:00")
print(m)