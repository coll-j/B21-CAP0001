from flask.json import jsonify
from entities.user_levels import UserLevels
from entities.level import Level
from adapters.helpers.token import Token
from adapters.helpers.session import session
from flask import jsonify

class LevelRepository:
    @staticmethod
    def levels(auth_header):
        user_id, auth_token, result = Token.get_token_and_user(auth_header=auth_header)
        if user_id:
            levels = []
            levels_temp = session.query(
                Level
            ).filter(
                UserLevels.level_id == Level.id
            ).filter(
                UserLevels.user_id == user_id
            ).all()

            for level in levels_temp:
                levels.append(level.as_dict())

            result["message"] = 'success'
            result["data"] = {
                'levels': levels
            }

            return result
        else:
            return result
