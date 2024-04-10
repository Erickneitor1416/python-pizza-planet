from faker import Faker

from app.plugins import db
from app.repositories.models import Beverage


def generate_fake_beverages(num_beverages):
    fake = Faker()
    beverages = []

    for _ in range(num_beverages):
        name = fake.word()
        price = fake.random.randrange(1, 10)

        beverage = Beverage(
            name=name,
            price=price,
        )
        beverages.append(beverage)

    db.session.add_all(beverages)
    db.session.commit()
