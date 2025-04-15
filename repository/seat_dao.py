from typing_inspection.typing_objects import is_classvar

from repository.base_repository import BaseRepository
from entity.seat import Seat


class SeatRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)


    def get_all(self) -> list[Seat]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seat")
            rows = cursor.fetchall()
            return [Seat(*row) for row in rows]


    def get(self, hall_id: str, row_number: int, seat_number: int) -> Seat:
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT isOccupied FROM seat WHERE hallID = %s AND rowNumber = %s AND seatNumber = %s",
                (hall_id, row_number, seat_number)
            )
            is_occupied = cursor.fetchone()[0]
            return Seat(hall_id, row_number, seat_number, is_occupied)


    def get_by_hall(self, hall_id: str) -> list[Seat]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seat WHERE hallID = %s", (hall_id,))
            rows = cursor.fetchall()
            return [Seat(*row) for row in rows]


    def get_by_hall_occupation(self, hall_id: str, is_occupied: bool):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM seat WHERE hallID = %s AND isOccupied = %s",
                (hall_id, is_occupied)
            )
            seats = cursor.fetchall()
            return [Seat(*row) for row in seats]


    def create(self, entity: Seat):
        self.execute_query(
            "INSERT INTO seat (hallID, rowNumber, seatNumber, isOccupied) VALUES (%s, %s, %s, %s)",
            (entity.get_hall_id(), entity.get_row_number(), entity.get_seat_number(), entity.is_occupied)
        )


    def update(self, entity: Seat):
        self.execute_query(
            "UPDATE seat SET isOccupied = %s WHERE hallID = %s AND rowNumber = %s AND seatNumber = %s",
            (entity.is_occupied, entity.get_hall_id(), entity.get_row_number(), entity.get_seat_number())
        )


    def delete(self, entity: Seat):
        self.execute_query(
            "DELETE FROM seat WHERE hallID = %s AND rowNumber = %s AND seatNumber = %s",
            (entity.get_hall_id(), entity.get_row_number(), entity.get_seat_number())
        )