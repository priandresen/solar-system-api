# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context

from dotenv import load_dotenv

from app import create_app, db
from app.models.planet import Planet

load_dotenv()

my_app = create_app()



with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="shiny, silver-white, and metallic.", orbital_period=88))
    db.session.add(Planet(name="Earth", description="rocky, blue-and-green sphere", orbital_period=365))
    db.session.add(Planet(name="Jupiter", description="colorful cloud bands, which are a mix of red, brown, yellow, and white", orbital_period=4333))
    db.session.add(Planet(name="Mars", description="rocky, desert-like world with a, dry surface", orbital_period=687))
    db.session.add(Planet(name="Saturn", description="a pale, yellowish-brown gas giant with prominent rings", orbital_period=10759))
    db.session.add(Planet(name="Uranus", description="gaseous cyan-coloured ice giant",orbital_period=30687))
    db.session.add(Planet(name="Neptune", description="deep, blue gas giant planet with a dynamic atmosphere", orbital_period=60190))
    db.session.add(Planet(name="Venus", description="a brilliant white or yellowish-white sphere", orbital_period=225))

    db.session.commit()


# planets = [
#     Planet(1, 'Mercury', 'shiny, silver-white, and metallic.', 0),
#     Planet(2, 'Earth', 'rocky, blue-and-green sphere', 1),
#     Planet(3, 'Jupiter', 'colorful cloud bands, which are a mix of red, brown, yellow, and white', 95),
#     Planet(4, 'Mars', 'rocky, desert-like world with a, dry surface', 2),
#     Planet(5, 'Saturn', 'a pale, yellowish-brown gas giant with prominent rings', 146),
#     Planet(6, 'Uranus', 'gaseous cyan-coloured ice giant', 28),   
#     Planet(7, 'Neptune', 'deep, blue gas giant planet with a dynamic atmosphere', 14),
#     Planet(8, 'Venus', 'a brilliant white or yellowish-white sphere', 0)
# ]
"""
Planet
Orbital Period (Earth Days)
Orbital Period (Earth Years)
Mercury
88
0.24
Venus
225
0.62
Earth
365
1
Mars
687
1.88
Jupiter
4,333
11.86
Saturn
10,759
29.46
Uranus
30,687
84.02
Neptune
60,190
164.79"""