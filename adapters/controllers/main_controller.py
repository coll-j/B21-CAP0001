from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.authentication_repository import AuthenticationRepository
main = Blueprint("main", __name__, url_prefix='/')

@main.route("", methods=["GET"])
def test():
  return "Your App Loades Successfully"
