from app.controllers import BeverageController
from app.factories.services.service_factory import ServiceFactory
from app.services.base import AbstractBaseService, BaseService


class BeverageServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> AbstractBaseService:
        return BaseService(BeverageController())
