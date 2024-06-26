from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple

from flask import Response, jsonify

from app.controllers import BaseController


class AbstractService(ABC):
    @staticmethod
    def _generate_response(
        value: Tuple[Response, str], error: str
    ) -> Tuple[Response, int]:
        response = value if not error else {"error": error}
        status_code = 200 if value else 404 if not error else 400
        return jsonify(response), status_code


class AbstractReportService(AbstractService):
    @abstractmethod
    def get_report(self) -> Tuple[Response, int]:
        pass


class AbstractBaseService(AbstractService):
    @abstractmethod
    def create(self, data: Optional[Any]) -> Tuple[Response, int]:
        pass

    @abstractmethod
    def update(self, data: Optional[Any]) -> Tuple[Response, int]:
        pass

    @abstractmethod
    def get_by_id(self, _id: int) -> Tuple[Response, int]:
        pass

    @abstractmethod
    def get_all(self) -> Tuple[Response, int]:
        pass


class BaseService(AbstractBaseService):
    def __init__(self, controller: BaseController):
        self.controller = controller

    def create(self, data: Optional[Any]) -> Tuple[Response, int]:
        value, error = self.controller.create(data)
        return self._generate_response(value, error)

    def update(self, data: Optional[Any]) -> Tuple[Response, int]:
        value, error = self.controller.update(data)
        return self._generate_response(value, error)

    def get_by_id(self, _id: int) -> Tuple[Response, int]:
        value, error = self.controller.get_by_id(_id)
        return self._generate_response(value, error)

    def get_all(self) -> Tuple[Response, int]:
        value, error = self.controller.get_all()
        return self._generate_response(value, error)
