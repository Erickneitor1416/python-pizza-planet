from app.controllers.size import SizeController
from app.factories.services import ServiceFactory
from app.services.base import AbstractBaseService, BaseService


class SizeServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> AbstractBaseService:
        return BaseService(SizeController())
