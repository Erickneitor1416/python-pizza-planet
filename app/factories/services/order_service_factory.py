from app.controllers import OrderController
from app.factories.services.service_factory import ServiceFactory
from app.services.base import BaseService


class OrderServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> BaseService:
        return BaseService(OrderController())
