from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, connection):
        self._connection = connection

    def execute_query(self, query: str, params: tuple):
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
        self._connection.commit()

    @abstractmethod
    def get_all(self):
        """Получение всех сущностей"""
        pass

    @abstractmethod
    def get(self, *keys):
        """Получение сущности по первичному ключу"""
        pass

    @abstractmethod
    def create(self, entity):
        """Добавление сущности в базу"""
        pass

    @abstractmethod
    def update(self, entity):
        """Обновление сущности"""
        pass

    @abstractmethod
    def delete(self, entity):
        """Удаление сущности"""
        pass
