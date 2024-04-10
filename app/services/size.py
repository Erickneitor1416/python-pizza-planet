from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT
from app.common.service_injector import get_singleton_service
from app.services.base import AbstractBaseService
from app.services.service_type import ServiceType

size = Blueprint(ServiceType.SIZE.value, __name__)

inject_service = get_singleton_service(ServiceType.SIZE)


@size.route("/", methods=POST)
@inject_service
def create_size(service: AbstractBaseService):
    return service.create(request.json)


@size.route("/", methods=PUT)
@inject_service
def update_size(service: AbstractBaseService):
    return service.update(request.json)


@size.route("/id/<_id>", methods=GET)
@inject_service
def get_size_by_id(service: AbstractBaseService, _id: int):
    return service.get_by_id(_id)


@size.route("/", methods=GET)
@inject_service
def get_all_sizes(service: AbstractBaseService):
    return service.get_all()
