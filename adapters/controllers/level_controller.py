from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.authentication_repository import AuthenticationRepository
level = Blueprint("level", __name__, url_prefix='/level/')

@level.route("/", methods=["GET"])
def levels():
  if request.method == "GET":
    auth_header = request.headers.get('Authorization')
    result = AuthenticationRepository.login(data['username'])

    return make_response(jsonify(result)), result["code"]
