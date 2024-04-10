from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT
from app.common.service_injector import get_singleton_service
from app.services.base import AbstractBaseService
from app.services.service_type import ServiceType

beverage = Blueprint(ServiceType.BEVERAGE.value, __name__)
inject_service = get_singleton_service(ServiceType.BEVERAGE)


@beverage.route("/", methods=POST)
@inject_service
def create_beverage(service: AbstractBaseService):
    return service.create(request.json)


@beverage.route("/", methods=PUT)
@inject_service
def update_beverage(service: AbstractBaseService):
    return service.update(request.json)


@beverage.route("/id/<_id>", methods=GET)
@inject_service
def get_beverage_by_id(service: AbstractBaseService, _id: int):
    return service.get_by_id(_id)


@beverage.route("/", methods=GET)
@inject_service
def get_beverages(service: AbstractBaseService):
    return service.get_all()
