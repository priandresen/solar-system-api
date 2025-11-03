from flask import Blueprint, request, abort, make_response, Response
from app.models.planet import Planet
from app.routes.route_utilities import validate_model
from app.db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.post('')
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)
    except KeyboardInterrupt as error:
        return {"error": f"Invalid request: missing: {error.args[0]}"}, 400
        

    db.session.add(new_planet)
    db.session.commit()    

    return new_planet.to_dict(), 201

@bp.get('')
def get_all_planets():

    description_param = request.args.get("description")
    moons_param = request.args.get("moons")
    name_param = request.args.get("name")
    query = db.select(Planet)

    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    if moons_param:
        query = query.where(Planet.moons >= moons_param)
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)


    return [planet.to_dict() for planet in planets]


@bp.get('/<id>')
def get_planet_by_id(id):
    planet = validate_model(Planet,id)

    return planet.to_dict()

@bp.put('/<id>')
def replace_planet(id):
    planet = validate_model(Planet, id)
    
    request_body = request.get_json()

    planet.name=request_body['name'],
    planet.description=request_body['description'],
    planet.moons=request_body['moons']
    db.session.commit()


    return Response(status=204, mimetype='application/json')

@bp.delete('/<id>')
def delete_planet_by_id(id):
    planet = validate_model(Planet,id)
    db.session.delete(planet)
    db.session.commit()

    # delete_response = ["Successfully deleted planet"]

    # return make_response(response, 204)
    return Response(status=204, mimetype="application/json")