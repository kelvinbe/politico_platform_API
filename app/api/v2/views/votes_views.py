#from flask_restful import Resource, Api
from error_handlers import create_404_response
from flask import Flask, Blueprint, make_response, request, jsonify
from ..models.votes_models import VotesModel
#from ..models.office_models import OfficeModel
version_2 = Blueprint('version_2', __name__, url_prefix='/api/v2/')


@version_2.route('/votes', methods=['POST'])
def vote():
    req = request.get_json()
    new = {
        "candidate": req['candidate'],
        "voter": req['voter'],
        "office": req['office']
    }

    reequest = VotesModel(**new)
    res = reequest.save()

    if isinstance(res, int):
        return make_response(jsonify({
            "message": "Voted",
            "vote_id": res
        }), 201)
    else:
        return make_response(jsonify({
            "message": "Vote already exists",
        }), 409)


@version_2.route('/votes/<int:id>', methods=['GET'])
def get(id):
    res = VotesModel().get_single_vote(id)
    if not res:
        return make_response(jsonify({
            "message": "Not found",
        }), 404)
    else:
        return make_response(jsonify({
            "message": "this is your vote",
            "votes": res
        }), 200)

@version_2.route('/votes/<int:id>', methods=['DELETE'])
def delete(id):
        delete = VotesModel()
        res = delete.delete_it("votes", "vote_id", id)
        if isinstance(res, int):

            return make_response(jsonify({
                "msg": "Deleted"
            }), 200)
        else:
            return make_response(jsonify({
                "msg": "Not found"

            }), 404)


