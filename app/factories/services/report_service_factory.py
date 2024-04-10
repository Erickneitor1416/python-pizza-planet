from typing import Any, Dict, Tuple

from app.controllers import ReportController
from app.factories.services.service_factory import ServiceFactory
from app.services.base import AbstractReportService, AbstractService


class ReportService(AbstractReportService):
    controller = ReportController()

    def get_report(self) -> Tuple[Dict[str, Any], int]:
        value, error = self.controller.get_report()
        return self._generate_response(value, error)


class ReportServiceFactory(ServiceFactory):
    @staticmethod
    def create_service() -> AbstractService:
        return ReportService()
