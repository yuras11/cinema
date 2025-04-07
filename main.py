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
from service.cast_member_service import CastMemberService
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


cc = MovieService(MovieDAO(connection))
c = cc.get_by_cast_member("e5227984-ccf5-408b-8f18-f8b43591a110")
print(c)