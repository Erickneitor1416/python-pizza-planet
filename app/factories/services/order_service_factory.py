from app.controllers import OrderController
from app.services.base import BaseService
from app.factories.services.service_factory import ServiceFactory


class OrderServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> BaseService:
        return BaseService(OrderController())
