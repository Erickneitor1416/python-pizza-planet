from faker import Faker

from app.plugins import db
from app.repositories.models import Beverage, Ingredient


def generate_ids_details():
    fake = Faker()
    num_details = fake.random_int(min=1, max=5)
    ingredient_ids = []
    beverage_ids = []
    for _ in range(num_details):
        ingredient = Ingredient.query.order_by(db.func.random()).first()
        ingredient_ids.append(ingredient._id)
        beverage = Beverage.query.order_by(db.func.random()).first()
        beverage_ids.append(beverage._id)

    return {
        "ingredients": beverage_ids,
        "beverages": ingredient_ids,
    }
