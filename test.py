import psycopg2

from repository.repos import CinemaSessionRepository
from service.cinema_session_service import CinemaSessionService

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


# from sqlalchemy import create_engine, select
# from orm.user_model import UserModel
# from orm.country_model import CountryModel, CountryNameModel
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
# Session = sessionmaker(engine)
#
# cinema_session_service = CinemaSessionService(CinemaSessionRepository, Session())
# print(cinema_session_service.get_by_date("2025-03-21")[0].movieid)

from repository.repos import UserRepository

print(UserRepository.get_all())