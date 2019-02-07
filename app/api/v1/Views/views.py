from flask import Flask, Blueprint, make_response, request, jsonify
from ..Models.models import PartyModels, OfficeModels
version_1 = Blueprint("version_1", __name__, url_prefix="/api/v1/")


@version_1.route('/parties', methods=['POST'])
def create_party():
    data = request.json
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']

    new_party = PartyModels().create(name, hqAddress, logoUrl)
    return make_response(jsonify({
        "status": 201,
        "msg": "party created successfully",
        "data": new_party

    }), 201)


@version_1.route('/parties', methods=['GET'])
def get_parties():
    parties = PartyModels().get_parties()
    return make_response(jsonify({
        "status": 200,
        "data": parties
    }), 200)


# View to get a specific party


@version_1.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    party = PartyModels().get_party(id)
    if party:
        return make_response(jsonify({
            "status": 200,
            "data": party
        }), 200)


# View to edit a specific party


@version_1.route('/parties/<int:id>/name', methods=['PATCH'])
def edit_party(id):
    data = request.json

    party = PartyModels().edit_party(id, data)
    return make_response(jsonify({
        "status": 200,
        "msg": "party edited successfully",
        "data": party
    }), 200)

   # View to delete a specific party


@version_1.route('/parties/<int:id>', methods=['DELETE'])
def delete_party(id):
    PartyModels().delete_party(id)
    return make_response(jsonify({
        "status": 200,
        "data": [{
            "Message": "party deleted successfully"
        }]
    }), 200)


