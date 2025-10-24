from flask import abort, Blueprint, make_response
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")





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

