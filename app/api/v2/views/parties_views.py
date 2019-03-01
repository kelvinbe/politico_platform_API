from error_handlers import create_404_response
from flask import Flask, Blueprint, make_response, request, jsonify
from ..models.parties_models import PartiesModel
parties = Blueprint('parties', __name__, url_prefix='/api/v2/')


@parties.route('/parties', methods=['POST'])
def party():
    req = request.get_json()
    new = {
        "name": req['name'],
        "hqAddress": req['hqAddress'],
        "logourl": req['logourl']
    }

    reequest = PartiesModel(**new)
    res = reequest.save()

    if isinstance(res, int):
        return make_response(jsonify({
            "message": "Party created",
            "party_id": res
        }), 201)
    else:
        return make_response(jsonify({
            "message": "Party already exists",
        }), 409)


@parties.route('/parties/result', methods=['GET'])
def get_parties():
    res = PartiesModel().get_parties()
    if not res:
        return make_response(jsonify({
            "message": "Database is empty"
        }), 404)
    else:
        return make_response(jsonify({
            "status": 200,
            "data": res
        }))


@parties.route('/parties/<int:id>/result', methods=['GET'])
def get(id):
    res = PartiesModel().get_single_party(id)
    if not res:
        return make_response(jsonify({
            "message": "Not found",
        }), 404)
    else:
        return make_response(jsonify({
            "status": 200,
            "data": res
        }), 200)
