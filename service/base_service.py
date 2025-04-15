from repository.base_repository import BaseRepository


class BaseService:
    def __init__(self, repository):
        self._repository = repository

    def get_all(self):
        """Получает все записи"""
        return self._repository.get_all()

    def get(self, *keys):
        """Получает запись по составному ключу"""
        return self._repository.get(*keys)

    def create(self, entity):
        """Создает новую запись"""
        return self._repository.create(entity)

    def update(self, entity):
        """Обновляет запись"""
        return self._repository.update(entity)

    def delete(self, *keys):
        """Удаляет запись"""
        return self._repository.delete(*keys)
