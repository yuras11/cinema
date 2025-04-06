from entity.base_entity import Entity


class Country(Entity):
    def __init__(self, country_code, language_code, country_name):
        super().__init__()
        self.__country_code = country_code
        self.__language_code = language_code
        self.__country_name = country_name

    def get_country_code(self):
        return self.__country_code

    def get_language_code(self):
        return self.__language_code

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, country_name):
        self.__country_name = country_name

    def to_dict(self) -> dict:
        return {
            '__country_code' : self.__country_code,
            '__language_code' : self.__language_code,
            '__country_name' : self.__country_name
        }

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return self.__country_name

    def __hash__(self):
        return hash((self.__country_code, self.__language_code, self.__country_name))

    def __str__(self):
        return self.__country_name