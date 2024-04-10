from app.controllers import IngredientController
from app.factories.services.service_factory import ServiceFactory
from app.services.base import AbstractBaseService, BaseService


class IngredientServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> AbstractBaseService:
        return BaseService(IngredientController())
