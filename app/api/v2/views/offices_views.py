from error_handlers import create_404_response
from flask import Flask, Blueprint, make_response, request, jsonify
from ..models.office_models import OfficeModel
offices = Blueprint('offices', __name__, url_prefix='/api/v2/')


@offices.route('/offices', methods=['POST'])
def office():
    req = request.get_json()
    new = {
        "name": req['name'],
        "type": req['type'],
        "user": req['user']
    }

    reequest = OfficeModel(**new)
    res = reequest.save()

    if isinstance(res, int):
        return make_response(jsonify({
            "message": "Office created",
            "office_id": res
        }), 201)
    else:
        return make_response(jsonify({
            "message": "Office already exists",
        }), 409)



@offices.route('/offices/result', methods=['GET'])
def get_offices():
    res = OfficeModel().get_offices()
    if not res:
        return make_response(jsonify({
            "message": "Database is empty"
        }), 404)
    else:
        return make_response(jsonify({
            "status": 200,
            "data": res
        }))


@offices.route('/offices/<int:id>', methods=['GET'])
def get(id):
    res = OfficeModel().get_single_office(id)
    if not res:
        return make_response(jsonify({
            "message": "Not found",
        }), 404)
    else:
        return make_response(jsonify({
            "status": 200,
            "data": res
        }), 200)