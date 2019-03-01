from flask import request, make_response, jsonify, Blueprint
from app.api.v2.models.user_models import UserModel
username = Blueprint('username', __name__, url_prefix='/api/v2/')

@username.route('/auth/candidate', methods=["POST"])
def candidate():
    req = request.get_json()
    new = {
        "username": req['username'],
        "password": req['password']
    }

    if UserModel().check_if_item_exists('users', 'username', new['username']) == False:
        return make_response(jsonify({
            "msg": "No such user"
        }), 401)

        record = UserModel().get_username_password(new['username'])
        user_id, password = record
        if password != new['password']:
            return make_response(jsonify({
                "msg": "username and password invalid"
            }), 401)
        token = UserModel().encode_token(user_id)
        return make_response(jsonify({
            "msg": "Welcome {}".format(new['username']),
            "access-token": token
        }), 200)


@username.route('/auth/register', methods=["POST"])
def user():
        req = request.get_json()
        new = {
            "name": req['name'],
            "username": req['username'],
            "password": req['password'],
            "email": req['email']
        }

        reequest = UserModel(**new)
        res = reequest.save()

        if isinstance(res, int):
            token = UserModel().encode_token(res)
            return make_response(jsonify({
                "msg": "Registered successfully",
                "access-token": token
            }), 201)
        else:
            return make_response(jsonify({
                "msg": "User already exists"
            }), 409)
