from enum import Enum


class ServiceType(Enum):
    ORDER = "order"
    BEVERAGE = "beverage"
    INGREDIENT = "ingredient"
    SIZE = "size"
    REPORT = "report"
