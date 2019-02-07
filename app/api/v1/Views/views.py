from flask import Flask, Blueprint, make_response, request, jsonify
from ..Models.models import PartyModels
version_1 = Blueprint("version_1", __name__, url_prefix="/api/v1/")


@version_1.route('/parties', methods=['POST'])
def create_party():
    data = request.json
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']

    new_party = PartyModels().create(name, hqAddress, logoUrl)
    return make_response(jsonify({
        "status": "OK",
        "msg": "party created successfully",
        "data": new_party

    }), 201)


@version_1.route('/parties', methods=['GET'])
def get_parties():
    parties = PartyModels().get_parties()
    return make_response(jsonify({
        "status": "OK",
        "data": parties
    }), 200)


# View to get a specific party


