from entity.base_entity import Entity


class CinemaSession(Entity):
    def __init__(self, movie, hall, date, time, ticket_fee, currency):
        super().__init__()
        self.__movie = movie
        self.__hall = hall
        self.__date = date
        self.__time = time
        self.__ticket_fee = ticket_fee
        self.__currency = currency

    def get_movie(self):
        return self.__movie

    def get_hall(self):
        return self.__hall

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def ticket_fee(self):
        return self.__ticket_fee

    @ticket_fee.setter
    def ticket_fee(self, ticket_fee):
        self.__ticket_fee = ticket_fee

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    def to_dict(self) -> dict:
        return {
            '__movie' : self.__movie,
            '__hall' : self.__hall,
            '__date' : self.__date,
            '__time' : self.__time,
            '__ticket_fee' : self.__ticket_fee,
            '__currency' : self.__currency
        }

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.__movie, self.__hall, self.__date, self.__time))

    # def __repr__(self):
    #     return f'{self.__movie.get_movie_name()}, {self.__hall.get_hall_name()}, {self.__date}, {self.__time}'

    def __str__(self):
        return f'{self.__movie.get_movie_name()}, {self.__hall.get_hall_name()}, {self.__date}, {self.__time}'