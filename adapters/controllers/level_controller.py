from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.level_repository import LevelRepository
level = Blueprint("level", __name__, url_prefix='/level/')

@level.route("/", methods=["GET"])
def levels():
    if request.method == "GET":
        auth_header = request.headers.get('Authorization')
        result = LevelRepository.levels(auth_header)

        return make_response(jsonify(result)), result["code"]

@level.route("/<level_id>", methods=["GET"])
def detail(level_id):
    if request.method == "GET":
        auth_header = request.headers.get('Authorization')
        result = LevelRepository.detail(level_id, auth_header)

        return make_response(jsonify(result)), result["code"]
