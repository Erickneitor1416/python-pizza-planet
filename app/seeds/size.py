from faker import Faker

from app.plugins import db
from app.repositories.models import Size


def generate_fake_sizes(num_sizes):
    fake = Faker()
    sizes = []

    for _ in range(num_sizes):
        name = fake.word()
        price = fake.random.randrange(1, 5)

        size = Size(
            name=name,
            price=price,
        )
        sizes.append(size)

    db.session.add_all(sizes)
    db.session.commit()
