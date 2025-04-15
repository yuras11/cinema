from entity.base_entity import Entity


class User(Entity):
    def __init__(self, user_id, login, password, name, surname, role):
        super().__init__()
        self.__user_id = user_id
        self.__login = login
        self.__password = password
        self.__name = name
        self.__surname = surname
        self.__role = role

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname


    def get_role(self):
        return self.__role


    def get_user_id(self):
        return self.__user_id


    def to_dict(self) -> dict:
        return {
            '__login' : self.__login,
            '__password' : self.__password,
            '__name' : self.__name,
            '__surname' : self.__surname
        }


    def __eq__(self, other):
        return self.get_user_id() == other.get_user_id()


    def __hash__(self):
        return hash(self.get_user_id())


    def __repr__(self):
        return f'{self.__name} {self.__surname}'


    def __str__(self):
        return f'{self.__name} {self.__surname}'