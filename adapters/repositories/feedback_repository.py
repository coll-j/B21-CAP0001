from adapters.repositories.check_token import check_token
from entities.level import Level
from entities.feedback import Feedback

class FeedbackRepository:
  @staticmethod
  def get_feedback(level_id, auth_header) -> dict:
    result = check_token(auth_header)

    if result['code'] == 200:
      feedback = Feedback.query.filter_by(level_id=level_id).first()
      if not feedback:
        result["message"] = 'Feedback not found'
        return result
      else:
        level = Level.query.filter_by(id=level_id).first()

        result["message"] = 'Feedback found'
        result["data"] = {
          'feedback': feedback,
          'level': level
        }
        return result
    else:
      return result