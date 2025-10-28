from flask import Blueprint, request, abort, make_response, Response
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

@planets_bp.get('')
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planet_response = []

    for planet in planets:
        planet_response.append({
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "moons" : planet.moons
        })

    return planet_response

def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        response = {'message': f'planet id {id} is invalid'}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id==id)
    # planet = db.session.get(Planet, id) ??????
    planet = db.session.scalar(query)

    if not planet:
        not_found = {'message': f'planet with id {id} not found'}
        abort(make_response(not_found, 404))

    return planet

@planets_bp.get('/<id>')
def get_planet_by_id(id):
    planet = validate_planet(id)

    response = {
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "moons" : planet.moons
    }

    return response

@planets_bp.put('/<id>')
def replace_planet(id):
    planet = validate_planet(id)
    
    request_body = request.get_json()

    planet.name=request_body['name'],
    planet.description=request_body['description'],
    planet.moons=request_body['moons']
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@planets_bp.delete('/<id>')
def delete_planet_by_id(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")