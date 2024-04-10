import pytest

from app.controllers.order import OrderController
from app.test.controllers.test_order import __create_sizes_and_ingredients, __order


@pytest.fixture
def report_uri():
    return "/report/"


@pytest.fixture
def init_report_test_data(ingredients, size, client_data):
    created_size, created_ingredients = __create_sizes_and_ingredients(
        ingredients, [size]
    )
    order = __order(created_ingredients, created_size, client_data)
    OrderController.create(order)
