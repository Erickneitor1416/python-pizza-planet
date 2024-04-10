from abc import ABC, abstractmethod

from app.services.base import AbstractService


class ServiceFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_service() -> AbstractService:
        pass
