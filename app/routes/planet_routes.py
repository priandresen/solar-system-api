from flask import Blueprint
from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get_all_planets('')
def get_all_planets():
    result = []

    for planet in planets:
        result.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            num_of_moons=planet.num_of_moons
        ))

    return result