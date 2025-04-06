from dao.base_dao import BaseDAO
from dao.movie_dao import MovieDAO
from dao.hall_dao import HallDAO
from entity.cinema_session import CinemaSession


class CinemaSessionDAO(BaseDAO):
    def __init__(self, connection):
        super().__init__(connection)
        self.__movie_dao = MovieDAO(connection)
        self.__hall_dao = HallDAO(connection)


    def __get_single_entry(self, cursor, movie_id, hall_id, date, time):
        cursor.execute(
            "SELECT ticketFee, currencyCode FROM cinema_session WHERE movieID = %s AND hallID = %s AND sessionDate = %s AND sessionTime = %s",
            (movie_id, hall_id, date, time)
        )
        ticket_fee, currency = cursor.fetchone()
        movie = self.__movie_dao.get(movie_id)
        hall = self.__hall_dao.get(hall_id)
        return CinemaSession(movie, hall, date, time, ticket_fee, currency)


    def get_all(self) -> list[CinemaSession]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT movieID, hallID, sessionDate, sessionTime FROM cinema_session")
            cinema_sessions = []

            for movie_id, hall_id, date, time in cursor.fetchall():
                cinema_sessions.append(self.__get_single_entry(cursor, movie_id, hall_id, date, time))

            return cinema_sessions


    def get(self, movie_id: str, hall_id: str, date: str, time: str) -> CinemaSession:
        with self._connection.cursor() as cursor:
            return self.__get_single_entry(cursor, movie_id, hall_id, date, time)


    def get_by_dates(self, start_date: str, end_date: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT movieID, hallID, sessionDate, sessionTime FROM cinema_session WHERE sessionDate BETWEEN %s AND %s",
                (start_date, end_date)
            )
            session_keys = cursor.fetchall()
            cinema_sessions = []
            for movie_id, hall_id, date, time in session_keys:
                cinema_sessions.append(self.__get_single_entry(cursor, movie_id, hall_id, date, time))
            return cinema_sessions


    def get_by_date(self, date: str) -> list[CinemaSession]:
        return self.get_by_dates(date, date)


    def get_by_movie_from_date_to_date(self, movie_id: str, start_date: str, end_date: str) -> list[CinemaSession]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT movieID, hallID, sessionDate, sessionTime
                FROM cinema_session
                WHERE movieID = %s
                AND sessionDate BETWEEN %s AND %s
                """,
                (movie_id, start_date, end_date)
            )
            session_keys = cursor.fetchall()
            cinema_sessions = []
            for movie_id, hall_id, date, time in session_keys:
                cinema_sessions.append(self.__get_single_entry(cursor, movie_id, hall_id, date, time))
            return cinema_sessions


    def get_by_hall_from_date_to_date(self, hall_id: str, start_date: str, end_date: str) -> list[CinemaSession]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT movieID, hallID, sessionDate, sessionTime 
                FROM cinema_session 
                WHERE hallID = %s
                AND sessionDate BETWEEN %s AND %s
                """,
                (hall_id, start_date, end_date)
            )
            session_keys = cursor.fetchall()
            cinema_sessions = []
            for movie_id, hall_id, date, time in session_keys:
                cinema_sessions.append(self.__get_single_entry(cursor, movie_id, hall_id, date, time))
            return cinema_sessions


    def create(self, entity: CinemaSession):
        self.execute_query(
            "INSERT INTO cinema_session (movieID, hallID, sessionDate, sessionTime, ticketFee, currency) VALUES (%s, %s, %s, %s, %s, %s)",
            (entity.get_movie().get_movie_id(), entity.get_hall().get_hall_id(), entity.date, entity.time, entity.ticket_fee, entity.currency)
        )


    def update(self, entity: CinemaSession):
        self.execute_query(
            "UPDATE cinema_session SET ticketFee = %s, currency = %s WHERE movieID = %s AND hallID = %s AND sessionDate = %s AND sessionTime = %s",
            (entity.ticket_fee, entity.currency, entity.get_movie().get_movie_id(), entity.get_hall().get_hall_id(), entity.date, entity.time)
        )


    def delete(self, entity: CinemaSession):
        self.execute_query(
            "DELETE FROM cinema_session WHERE movieID = %s AND hallID = %s AND sessionDate = %s AND sessionTime = %s",
            (entity.get_movie().get_movie_id(), entity.get_hall().get_hall_id(), entity.date, entity.time)
        )