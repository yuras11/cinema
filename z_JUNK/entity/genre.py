from z_JUNK.entity.base_entity import Entity


class Genre(Entity):
    def __init__(self, genre_id, language_code, genre_name):
        super().__init__()
        self.__genre_id = genre_id
        self.__language_code = language_code
        self.__genre_name = genre_name


    def get_genre_id(self):
        return self.__genre_id


    def get_language_code(self):
        return self.__language_code

    @property
    def genre_name(self):
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name):
        self.__genre_name = genre_name


    def to_dict(self) -> dict:
        return {
            '__genre_id': self.__genre_id,
            '__language_code': self.__language_code,
            '__genre_name': self.__genre_name
        }

    def __eq__(self, other):
        return self.get_genre_id() == other.get_genre_id()


    def __hash__(self):
        return hash(self.get_genre_id())


    def __repr__(self):
        return str(self.to_dict())


    def __str__(self):
        return str(self.to_dict())