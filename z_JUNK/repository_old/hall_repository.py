from z_JUNK.repository_old.base_repository import BaseRepository
from z_JUNK.repository_old.seat_repository import SeatRepository
from z_JUNK.entity.hall import Hall

lang = 'RU'

class HallRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self.__seat_dao = SeatRepository(connection)


    def __get_single_entry(self, cursor, hall_id):
        cursor.execute(
            "SELECT capacity FROM hall WHERE hallID = %s",
            (hall_id,)
        )
        capacity = cursor.fetchone()[0]
        cursor.execute(
            "SELECT hallName FROM hall_names WHERE hallID = %s AND languageCode = %s",
            (hall_id, lang)
        )
        hall_name = cursor.fetchone()[0].strip()
        hall_seats = self.__seat_dao.get_by_hall(hall_id)
        return Hall(hall_id, hall_name, capacity, hall_seats)


    def get_all(self) -> list[Hall]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT hallID FROM hall")
            hall_ids = [row[0] for row in cursor.fetchall()]
            halls_list = []
            for hall_id in hall_ids:
                halls_list.append(self.__get_single_entry(cursor, hall_id))
            return halls_list


    def get(self, hall_id: str) -> Hall:
        with self._connection.cursor() as cursor:
            return self.__get_single_entry(cursor, hall_id)


    def create(self, entity: Hall):
        self.execute_query(
            "INSERT INTO hall (hallID, capacity) VALUES (%s, %s)",
            (entity.get_hall_id(), entity.get_capacity())
        )
        self.execute_query(
            "INSERT INTO hall_names (hallID, languageCode, hallName) VALUES (%s, %s, %s)",
            (entity.get_hall_id(), lang, entity.get_hall_name())
        )
        for seat in entity.get_hall_seats():
            self.execute_query(
                "INSERT INTO seat (hallID, rowNumber, seatNumber, isOccupied) VALUES (%s, %s, %s, %s)",
                (entity.get_hall_id(), seat.get_row_number(), seat.get_seat_number(), seat.is_occupied)
            )


    def update(self, entity: Hall):
        self.execute_query(
            "UPDATE hall_names SET hallName = %s WHERE hallID = %s and languageCode = %s",
            (entity.get_hall_name(), entity.get_hall_id(), lang)
        )


    def delete(self, entity: Hall):
        self.execute_query(
            "DELETE FROM hall WHERE hallID = %s",
            (entity.get_hall_id(),)
        )