from flask import Blueprint, request
from adapters.repositories.authentication_repository import AuthenticationRepository
authentication = Blueprint("authentication", __name__, url_prefix='/auth')

@authentication.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        user = AuthenticationRepository.login(data['username'])
        return user, 200
