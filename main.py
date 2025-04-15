import psycopg2
import uuid

from repository.cast_member_repository import CastMemberRepository
from repository.cinema_session_repository import CinemaSessionRepository
from repository.country_repository import CountryRepository
from repository.genre_repository import GenreRepository
from repository.hall_repository import HallRepository
from repository.movie_repository import MovieRepository
from repository.position_repository import PositionRepository
from repository.seat_repository import SeatRepository
from repository.user_repository import UserRepository
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