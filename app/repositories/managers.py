from typing import Any, List, Optional, Sequence

from sqlalchemy import desc, extract, func
from sqlalchemy.sql import column, text

from .models import Beverage, Ingredient, Order, OrderDetail, Size, db
from .serializers import (
    BeverageSerializer,
    IngredientSerializer,
    OrderSerializer,
    SizeSerializer,
    ma,
)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(
        cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]
    ):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                )
                for ingredient in ingredients
            )
        )
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                )
                for beverage in beverages
            )
        )
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f"Method not suported for {cls.__name__}")


class ReportManager:
    session = db.session

    @classmethod
    def get_best_customers(cls):
        best_customers = (
            cls.session.query(
                Order.client_name,
                func.count(Order.client_name).label("orders_count"),
                func.sum(Order.total_price).label("total_spent"),
            )
            .group_by(Order.client_name)
            .order_by(func.sum(Order.total_price).desc())
            .limit(3)
            .all()
        )
        return [
            {
                "client_name": customer[0],
                "orders_count": customer[1],
                "total_spent": customer[2],
            }
            for customer in best_customers
        ]

    @classmethod
    def get_highest_revenue_by_month(cls):

        revenue = (
            cls.session.query(
                extract("month", Order.date).label("month"),
                func.sum(Order.total_price).label("total_revenue"),
            )
            .group_by("month")
            .order_by(desc("total_revenue"))
            .first()
        )
        if revenue:
            return {"month": revenue[0], "revenue": revenue[1]}
        else:
            return None

    @classmethod
    def get_most_requested_ingredient_id(cls):
        ingredient_counts = (
            cls.session.query(Ingredient._id, func.count(Ingredient._id))
            .group_by(Ingredient._id)
            .order_by(func.count(Ingredient._id).desc())
            .first()
        )
        return ingredient_counts[0]


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column("1")).from_statement(text("SELECT 1")).all()
