from flask import Blueprint, request

from app.common.http_methods import GET, POST
from app.common.service_injector import get_singleton_service
from app.services.base import AbstractBaseService
from app.services.service_type import ServiceType

order = Blueprint(ServiceType.ORDER.value, __name__)
inject_service = get_singleton_service(ServiceType.ORDER)


@order.route("/", methods=POST)
@inject_service
def create_order(service: AbstractBaseService):
    return service.create(request.json)


@order.route("/id/<_id>", methods=GET)
@inject_service
def get_order_by_id(service: AbstractBaseService, _id: int):
    return service.get_by_id(_id)


@order.route("/", methods=GET)
@inject_service
def get_orders(service: AbstractBaseService):
    return service.get_all()
