from faker import Faker

from app.plugins import db
from app.repositories.models import Ingredient


def generate_fake_ingredients(num_ingredients):
    fake = Faker()
    ingredients = []

    for _ in range(num_ingredients):
        name = fake.word()
        price = fake.random.randrange(1, 10)

        ingredient = Ingredient(
            name=name,
            price=price,
        )
        ingredients.append(ingredient)

    db.session.add_all(ingredients)
    db.session.commit()
