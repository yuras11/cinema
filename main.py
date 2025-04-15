import psycopg2
import uuid

from repository.cast_member_dao import CastMemberRepository
from repository.cinema_session_dao import CinemaSessionRepository
from repository.country_dao import CountryRepository
from repository.genre_dao import GenreRepository
from repository.hall_dao import HallRepository
from repository.movie_dao import MovieRepository
from repository.position_dao import PositionRepository
from repository.seat_dao import SeatRepository
from repository.user_dao import UserRepository
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


cmd = CastMemberRepository(connection)
cast_member = cmd.get_by_name('Мэттью Макконахи')
print(cast_member)