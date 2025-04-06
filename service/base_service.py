from dao.base_dao import BaseDAO
from typing import Generic, TypeVar


class BaseService:
    def __init__(self, dao):
        self._dao = dao

    def get_all(self):
        """Получает все записи"""
        return self._dao.get_all()

    def get(self, *keys):
        """Получает запись по составному ключу"""
        return self._dao.get(*keys)

    def create(self, entity):
        """Создает новую запись"""
        return self._dao.create(entity)

    def update(self, entity):
        """Обновляет запись"""
        return self._dao.update(entity)

    def delete(self, *keys):
        """Удаляет запись"""
        return self._dao.delete(*keys)
