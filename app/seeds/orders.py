from faker import Faker

from app.controllers.order import OrderController
from app.plugins import db
from app.repositories.models import Size
from app.seeds.client import generate_fake_client_data
from app.seeds.orderDetails import generate_ids_details


def generate_fake_orders(num_people):
    fake = Faker()
    orders = []
    error = None

    while len(orders) < num_people:
        order_count = fake.random_int(min=1, max=10)
        client_data = generate_fake_client_data()
        for _ in range(order_count):
            order, order_error = create_order(fake, client_data)
            if order_error:
                error = order_error
            orders.append(order)
            if len(orders) >= num_people:
                break

    print(f"Generated {len(orders)} orders.")
    return orders, error


def create_order(fake, client_data):
    order_data = generate_order_data(fake, client_data)
    details = generate_ids_details()
    order = {**order_data, **details}
    return OrderController.create(order)


def generate_order_data(fake, client_data):
    order_date = fake.date_time_between(start_date="-6M", end_date="now")
    size_id = Size.query.order_by(db.func.random()).first()._id
    return {
        **client_data,
        "date": order_date,
        "size_id": size_id,
    }
