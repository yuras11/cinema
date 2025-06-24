from z_JUNK.entity.base_entity import Entity


class Hall(Entity):
    MAX_SEATS_IN_A_SINGLE_ROW = 10

    def __init__(self, hall_id, hall_name, capacity, hall_seats):
        super().__init__()
        self.__hall_id = hall_id
        self.__hall_name = hall_name
        self.__capacity = capacity
        self.__hall_seats = hall_seats


    def get_hall_id(self):
        return self.__hall_id


    def get_capacity(self):
        return self.__capacity


    def get_hall_name(self):
        return self.__hall_name


    def get_hall_seats(self):
        return self.__hall_seats


    def to_dict(self) -> dict:
        return {
            '__hall_id' : self.__hall_id,
            '__hall_name' : self.__hall_name,
            '__capacity' : self.__capacity,
            '__hall_seats': self.__hall_seats
        }


    def __eq__(self, other):
        return self.get_hall_id() == other.get_hall_id()


    def __hash__(self):
        return hash(self.get_hall_id())


    def __str__(self):
        return str(self.to_dict())


    def __repr__(self):
        return str(self.to_dict())