from typing import Any, Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError

from app.repositories.managers import IngredientManager, ReportManager


class ReportController:
    manager = ReportManager

    @classmethod
    def get_report(cls) -> Tuple[Any, Optional[str]]:
        try:
            return {
                "best_customers": cls.get_best_customers(),
                "highest_revenue_by_month": cls.get_highest_revenue_by_month(),
                "most_requested_ingredient": cls.get_most_requested_ingredient(),
            }, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_best_customers(cls):
        return cls.manager.get_best_customers()

    @classmethod
    def get_highest_revenue_by_month(cls):
        return cls.manager.get_highest_revenue_by_month()

    @classmethod
    def get_most_requested_ingredient(cls):
        ingredient_id = cls.manager.get_most_requested_ingredient_id()
        return IngredientManager.get_by_id(ingredient_id)
