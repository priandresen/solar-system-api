# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context

from app import create_app, db
from app.models.planet import Planet
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()



with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="shiny, silver-white, and metallic.", moons=0))
    db.session.add(Planet(name="Earth", description="rocky, blue-and-green sphere", moons=1))
    db.session.add(Planet(name="Jupiter", description="colorful cloud bands, which are a mix of red, brown, yellow, and white", moons=95))
    db.session.add(Planet(name="Mars", description="rocky, desert-like world with a, dry surface", moons=2))
    db.session.add(Planet(name="Saturn", description="a pale, yellowish-brown gas giant with prominent rings", moons=146))
    db.session.add(Planet(name="Uranus", description="gaseous cyan-coloured ice giant", moons=28))
    db.session.add(Planet(name="Neptune", description="deep, blue gas giant planet with a dynamic atmosphere", moons=14))
    db.session.add(Planet(name="Venus", description="a brilliant white or yellowish-white sphere", moons=0))

    db.session.commit()