from functools import wraps

from app.factories import (
    BeverageServiceFactory,
    IngredientServiceFactory,
    OrderServiceFactory,
    ReportServiceFactory,
    ServiceFactory,
    SizeServiceFactory,
)
from app.services.service_type import ServiceType

factories = {
    ServiceType.SIZE: SizeServiceFactory,
    ServiceType.INGREDIENT: IngredientServiceFactory,
    ServiceType.ORDER: OrderServiceFactory,
    ServiceType.REPORT: ReportServiceFactory,
    ServiceType.BEVERAGE: BeverageServiceFactory,
}


def get_singleton_service(service_type: ServiceType):
    _service_instance = {}

    def inject_service(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if service_type not in _service_instance:
                service_factory: ServiceFactory = factories.get(service_type)
                _service_instance[service_type] = service_factory.create_service()
            service = _service_instance[service_type]
            return func(service, *args, **kwargs)

        return wrapper

    return inject_service
