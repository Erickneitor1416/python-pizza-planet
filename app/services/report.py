from flask import Blueprint

from app.common.http_methods import GET
from app.common.service_injector import get_singleton_service
from app.services.base import AbstractReportService
from app.services.service_type import ServiceType

report = Blueprint(ServiceType.REPORT.value, __name__)
inject_service = get_singleton_service(ServiceType.REPORT)


@report.route("/", methods=GET)
@inject_service
def get_report(service: AbstractReportService):
    return service.get_report()
