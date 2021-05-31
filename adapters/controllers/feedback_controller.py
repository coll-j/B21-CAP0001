from adapters.repositories.feedback_repository import FeedbackRepository
from flask import Blueprint, request, make_response
from flask.json import jsonify
feedback = Blueprint("feedback", __name__, url_prefix='/feedback/')

@feedback.route('/<level_id>', methods=["GET"])
def get_feedback(level_id):
  auth_header = request.headers.get('Authorization')
  result = FeedbackRepository.get_feedback(level_id, auth_header)

  return make_response(jsonify(result)), result["code"]
