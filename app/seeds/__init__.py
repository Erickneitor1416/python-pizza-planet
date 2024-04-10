from app.seeds.beverages import generate_fake_beverages
from app.seeds.ingredients import generate_fake_ingredients
from app.seeds.orders import generate_fake_orders
from app.seeds.size import generate_fake_sizes


def generate_fake_data():
    generate_fake_beverages(10)
    generate_fake_ingredients(10)
    generate_fake_sizes(5)
    return generate_fake_orders(100)
