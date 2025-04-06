from entity.base_entity import Entity


class CastMember(Entity):
    def __init__(self, member_id, member_name, date_of_birth, country, member_positions):
        super().__init__()
        self.__member_id = member_id
        self.__member_name = member_name
        self.__date_of_birth = date_of_birth
        self.__country = country
        self.__member_positions = member_positions

    def get_member_id(self):
        return self.__member_id

    @property
    def member_name(self):
        return self.__member_name

    @member_name.setter
    def member_name(self, member_name):
        self.__member_name = member_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_country(self):
        return self.__country

    def get_member_positions(self):
        return self.__member_positions

    def to_dict(self) -> dict:
        return {
            '__member_id' : self.__member_id,
            '__member_name' : self.__member_name,
            '__date_of_birth' : self.__date_of_birth,
            '__country' : self.__country,
            '__member_positions' : self.__member_positions
        }

    def __eq__(self, other):
        return self.__member_id == other.get_member_id()

    def __hash__(self):
        pass

    def __repr__(self):
        return self.__member_name

    def __str__(self):
        return self.__member_name