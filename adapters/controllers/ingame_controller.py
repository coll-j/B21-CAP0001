from adapters.repositories.feedback_repository import FeedbackRepository
from flask import Blueprint, request, make_response
from flask.json import jsonify
ingame = Blueprint("ingame", __name__, url_prefix='/ingame/')

@ingame.route('/save', methods=["POST"])
def save_game(level_id):
  auth_header = request.headers.get('Authorization')
  result = FeedbackRepository.get_feedback(level_id, auth_header)

  return make_response(jsonify(result)), result["code"]
