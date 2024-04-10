import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db

# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size
from app.seeds import generate_fake_data

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command("populate")
def populate():
    responses, error = generate_fake_data()
    if error:
        print(f"Error: {error}")
    else:
        print(f"{len(responses)} orders have been created")


@manager.command("test", with_appcontext=False)
def test():
    return pytest.main(["-v", "./app/test"])


if __name__ == "__main__":
    manager()
