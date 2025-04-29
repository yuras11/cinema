from abc import ABC, abstractmethod
from sqlalchemy.orm.session import Session
from config import Session

class Repository(ABC):
    def __init__(self):
        self._session = Session()

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, *keys):
        pass


    def insert(self, model):
        with self._session as session:
            session.add(model)
            session.commit()


    def update(self, model):
        with self._session as session:
            session.merge(model)
            session.commit()


    def delete(self, model):
        with self._session as session:
            session.delete(model)
            session.commit()