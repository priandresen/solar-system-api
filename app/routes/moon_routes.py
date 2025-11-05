from flask import Blueprint, request, Response
from app.models.moon import Moon
from app.routes.route_utilities import get_model_with_filters, validate_model, create_model
from app.db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/moons")


@bp.post('')
def create_moons():
    request_body = request.get_json()

    return create_model(Moon, request_body)

@bp.get('')
def get_all_moons():

    return get_model_with_filters(Moon, request.args)

@bp.get('/<id>')
def get_moon_by_id(id):
    moon = validate_model(Moon,id)

    return moon.to_dict()

@bp.put('/<id>')
def replace_moon(id):
    moon = validate_model(Moon, id)
    
    request_body = request.get_json()

    moon.size=request_body['size'],
    moon.description=request_body['description'],
    moon.ring=request_body['rings']
    db.session.commit()


    return Response(status=204, mimetype='application/json')

@bp.delete('/<id>')
def delete_moon_by_id(id):
    moon = validate_model(Moon,id)
    db.session.delete(moon)
    db.session.commit()

    # delete_response = ["Successfully deleted moon"]
    # return make_response(response, 204)
    
    return Response(status=204, mimetype="application/json")