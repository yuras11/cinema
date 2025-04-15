from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Converts object to a dictionary"""
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
    