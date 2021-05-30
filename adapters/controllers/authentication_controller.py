from flask import Blueprint, request, make_response
from flask.json import jsonify
from adapters.repositories.authentication_repository import AuthenticationRepository
authentication = Blueprint("authentication", __name__, url_prefix='/auth/')

@authentication.route("/login", methods=["POST"])
def login():
  if request.method == "POST":
    data = request.get_json()
    result = AuthenticationRepository.login(data['username'])
    
    if(result["code"] == 401):
      return make_response(jsonify(result)), 401
    elif(result["code"] == 200):
      return make_response(jsonify(result)), 200
    elif(result["code"] == 500):
      return make_response(jsonify(result)), 500

@authentication.route('/register', methods=["POST"])
def register():
  if request.method == "POST":
    data = request.get_json()
    result = AuthenticationRepository.register(data["email"], data["username"], data["password"])
    
    if(result["code"] == 401):
      return make_response(jsonify(result)), 401
    elif(result["code"] == 202):
      return make_response(jsonify(result)), 202
    elif(result["code"] == 201):
      return make_response(jsonify(result)), 201



@authentication.route('/logout', methods=['POST'])
def logout():
  if request.method == "POST":
    auth_header = request.headers.get('Authorization')
    result = AuthenticationRepository.logout(auth_header)

    if(result["code"] == 401):
      return make_response(jsonify(result)), 401
    elif(result["code"] == 200):
      return make_response(jsonify(result)), 200
    elif(result["code"] == 403):
      return make_response(jsonify(result)), 403