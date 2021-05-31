from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.authentication_repository import AuthenticationRepository
authentication = Blueprint("authentication", __name__, url_prefix='/auth/')

@authentication.route("/login", methods=["POST"])
def login():
  data = request.get_json()
  result = AuthenticationRepository.login(data['username'])
  
  return make_response(jsonify(result)), result["code"]
    
@authentication.route('/register', methods=["POST"])
def register():
  data = request.get_json()
  result = AuthenticationRepository.register(data["email"], data["username"], data["password"])

  return make_response(jsonify(result)), result["code"]



@authentication.route('/logout', methods=['POST'])
def logout():
  auth_header = request.headers.get('Authorization')
  result = AuthenticationRepository.logout(auth_header)

  return make_response(jsonify(result)), result["code"]