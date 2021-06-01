from flask.json import jsonify
from entities.user_badge import UserBadge
from entities.badge import Badge
from adapters.helpers.token import Token
from adapters.helpers.session import session
from flask import jsonify

class BadgeRepository:
    @staticmethod
    def badges(auth_header):
        user_id, auth_token, result = Token.get_token_and_user(auth_header=auth_header)
        if user_id:
            badges = []
            badges_temp = session.query(
                Badge
            ).filter(
                UserBadge.badge_id == Badge.id
            ).filter(
                UserBadge.user_id == user_id
            ).all()

            for badge in badges_temp:
                badges.append(badge.as_dict())

            result["message"] = 'success'
            result["data"] = {
                'badges': badges
            }

            return result
        else:
            return result
