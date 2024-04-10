from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT
from app.common.service_injector import get_singleton_service
from app.services.base import AbstractBaseService
from app.services.service_type import ServiceType

ingredient = Blueprint(ServiceType.INGREDIENT.value, __name__)
inject_service = get_singleton_service(ServiceType.INGREDIENT)


@ingredient.route("/", methods=POST)
@inject_service
def create_ingredient(service: AbstractBaseService):
    return service.create(request.json)


@ingredient.route("/", methods=PUT)
@inject_service
def update_ingredient(service: AbstractBaseService):
    return service.update(request.json)


@ingredient.route("/id/<_id>", methods=GET)
@inject_service
def get_ingredient_by_id(service: AbstractBaseService, _id: int):
    return service.get_by_id(_id)


@ingredient.route("/", methods=GET)
@inject_service
def get_ingredients(service: AbstractBaseService):
    return service.get_all()
