from flask import Blueprint, request

authentication = Blueprint("authentication", __name__, url_prefix='/auth')

@authentication.route("/login", methods=["GET"])
def login():
  if request.method == "GET":
    return "coba"
