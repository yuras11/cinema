from entity.base_entity import Entity


class Seat(Entity):
    def __init__(self, hall_id, row_number, seat_number, is_occupied):
        super().__init__()
        self.__hall_id = hall_id
        self.__row_number = row_number
        self.__seat_number = seat_number
        self.__is_occupied = is_occupied

    def get_hall_id(self):
        return self.__hall_id

    def get_row_number(self):
        return self.__row_number

    def get_seat_number(self):
        return self.__seat_number

    @property
    def is_occupied(self):
        return self.__is_occupied

    @is_occupied.setter
    def is_occupied(self, is_occupied):
        self.__is_occupied = is_occupied

    def to_dict(self) -> dict:
        return {
            '__hall_id' : self.__hall_id,
            '__row_number' : self.__row_number,
            '__seat_number' : self.__seat_number,
            '__is_occupied' : self.__is_occupied
        }

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.__hall_id, self.__row_number, self.__seat_number))

    def __str__(self):
        return f'{self.__row_number} ряд - {self.__seat_number} место'