from entity.base_entity import Entity


class Movie(Entity):
    def __init__(self, movie_id, movie_name, movie_countries, movie_genres, movie_cast, duration, release_date, age_rate):
        super().__init__()
        self.__movie_id = movie_id
        self.__movie_name = movie_name
        self.__movie_countries = movie_countries
        self.__movie_genres = movie_genres
        self.__movie_cast = movie_cast
        self.__duration = duration
        self.__release_date = release_date
        self.__age_rate = age_rate

    def get_movie_id(self):
        return self.__movie_id


    def get_movie_name(self):
        return self.__movie_name

    def get_movie_countries(self):
        return self.__movie_countries

    def get_movie_cast(self):
        return self.__movie_cast

    def get_movie_genres(self):
        return self.__movie_genres

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def get_release_date(self):
        return self.__release_date

    def get_age_rate(self):
        return self.__age_rate

    def to_dict(self) -> dict:
        return {
            '__movie_id' : self.__movie_id,
            '__movie_name' : self.__movie_name,
            '__movie_countries' : self.__movie_countries,
            '__movie_genres' : self.__movie_genres,
            '__movie_cast' : self.__movie_cast,
            '__duration' : self.__duration,
            '__release_date' : self.__release_date,
            '__age_rate' : self.__age_rate
        }

    def __eq__(self, other):
        return self.__movie_id == other.get_movie_id()

    def __hash__(self):
        pass

    def __repr__(self):
        return self.__movie_name

    def __str__(self):
        return self.get_movie_name()