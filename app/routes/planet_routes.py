from flask import Blueprint, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.route_utilities import get_model_with_filters, validate_model, create_model
from app.db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.post('')
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body).to_dict()

@bp.post('<id>/moons')
def create_moon_associated_with_a_planet(id):
    request_body = request.get_json()
    planet = validate_model(Planet, id)
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body).to_dict()

@bp.get('')
def get_all_planets():

    return get_model_with_filters(Planet, request.args)

@bp.get('/<id>')
def get_planet_by_id(id):
    planet = validate_model(Planet,id)

    return planet.to_dict()

@bp.get("/<id>/moons")
def get_planet_by_id_with_moons(id):
    
    planet = validate_model(Planet,id)
    moons = []
    for moon in planet.moons:
        moons.append(moon.to_dict())

    return moons

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