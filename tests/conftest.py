import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    }

    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
#this client fixture can be used in test files to make requests to the app
#it simulates a real client without running the server

@pytest.fixture
def one_planet(app):
    planet = Planet(
        name="Earth", 
        description="rocky, blue-and-green sphere", 
        moons=1
    )
    db.session.add(planet)
    db.session.commit()
    return planet
