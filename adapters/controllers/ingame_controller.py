from adapters.repositories.ingame_repository import InGameRepository
from adapters.repositories.feedback_repository import FeedbackRepository
from flask import Blueprint, request, make_response
from flask.json import jsonify
ingame = Blueprint("ingame", __name__, url_prefix='/ingame/')

@ingame.route('/save', methods=["POST"])
def save_game():
  data = request.get_json()
  auth_header = request.headers.get('Authorization')
  result = InGameRepository.save_game(data['user_id'], data['level_id'], auth_header)

  return make_response(jsonify(result)), result["code"]

@ingame.route('/saved-list/<user_id>', methods=["GET"])
def get_saved_game(user_id):
  auth_header = request.headers.get('Authorization')
  result = InGameRepository.get_saved_game(user_id, auth_header)

  return make_response(jsonify(result)), result["code"]
