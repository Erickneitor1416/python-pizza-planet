from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

from flask import jsonify, Response

from app.controllers import BaseController


class AbstractService(ABC):
    @staticmethod
    def _generate_response(
            value: Dict[str, Any], error: str
    ) -> Tuple[Response, int]:
        response = value if not error else {"error": error}
        status_code = 200 if value else 404 if not error else 400
        return jsonify(response), status_code


class AbstractReportService(AbstractService):
    @abstractmethod
    def get_report(self) -> Tuple[Dict[str, Any], int]:
        pass


class AbstractBaseService(AbstractService):
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        pass

    @abstractmethod
    def update(self, data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        pass

    @abstractmethod
    def get_by_id(self, _id: int) -> Tuple[Dict[str, Any], int]:
        pass

    @abstractmethod
    def get_all(self) -> Tuple[Dict[str, Any], int]:
        pass


class BaseService(AbstractBaseService):
    def __init__(self, controller: BaseController):
        self.controller = controller

    def create(self, data: Dict[str, Any]) -> Tuple[Response, int]:
        value, error = self.controller.create(data)
        return self._generate_response(value, error)

    def update(self, data: Dict[str, Any]) -> Tuple[Response, int]:
        value, error = self.controller.update(data)
        return self._generate_response(value, error)

    def get_by_id(self, _id: int) -> Tuple[Response, int]:
        value, error = self.controller.get_by_id(_id)
        return self._generate_response(value, error)

    def get_all(self) -> Tuple[Response, int]:
        value, error = self.controller.get_all()
        return self._generate_response(value, error)
