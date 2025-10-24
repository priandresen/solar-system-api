from flask import abort, Blueprint, request
from app.models.planet import Planet
from app.db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.post('')
def create_planet():
    request_body = request.get_json()
    
    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        moons=request_body['moons']
    )

    db.session.add(new_planet)
    db.session.commit()    

    response = {
        "id" : new_planet.id,
        "name" : new_planet.name,
        "description" : new_planet.description,
        "moons" : new_planet.moons
    }

    return response, 201


# @planets_bp.get('')
# def get_all_planets():
#     result = []

#     for planet in planets:
#         result.append(dict(
#             id=planet.id,
#             name=planet.name,
#             description=planet.description,
#             num_of_moons=planet.num_of_moons
#         ))

#     return result

# @planets_bp.get('/<id>')
# def get_single_planet(id):

#     planet = validate_planet(id)

#     planet_dict = dict (
#         id=planet.id,
#         name=planet.name,
#         description=planet.description,
#         num_of_moons=planet.num_of_moons
#     )
    
#     return planet_dict

# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         response = {'message': f'planet id {id} is invalid'}

#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet
    
#     not_found = {'message': f'planet with id {id} not found'}
#     abort(make_response(not_found, 404))

