from entity.base_entity import Entity


class Position(Entity):
    def __init__(self, position_id, language_code, position_name):
        super().__init__()
        self.__position_id = position_id
        self.__language_code = language_code
        self.__position_name = position_name

    def get_position_id(self):
        return self.__position_id

    def get_language_code(self):
        return self.__language_code

    @property
    def position_name(self):
        return self.__position_name

    @position_name.setter
    def position_name(self, position_name):
        self.__position_name = position_name

    def to_dict(self) -> dict:
        return {
            '__position_id' : self.__position_id,
            '__language_code' : self.__language_code,
            '__position_name' : self.__position_name
        }

    def __eq__(self, other):
        return self.__position_id == other.get_position_id()

    def __hash__(self):
        pass

    def __repr__(self):
        return self.__position_name

    def __str__(self):
        return self.__position_name