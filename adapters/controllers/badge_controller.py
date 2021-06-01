from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.badge_repository import BadgeRepository
badge = Blueprint("badge", __name__, url_prefix='/badge/')

@badge.route("/", methods=["GET"])
def badges():
    if request.method == "GET":
        auth_header = request.headers.get('Authorization')
        result = BadgeRepository.badges(auth_header)

        return make_response(jsonify(result)), result["code"]
