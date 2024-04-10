from app.controllers import IngredientController
from app.services.base import AbstractBaseService, BaseService
from app.factories.services.service_factory import ServiceFactory


class IngredientServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> AbstractBaseService:
        return BaseService(IngredientController())
