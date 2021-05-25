from http import HTTPStatus
from flask import jsonify


def handle_success(data):
    message = "success"
    return jsonify({"message": message, "data": data}), HTTPStatus.OK


def handle_validation_error(e):
    return jsonify({"message": e.message}), HTTPStatus.BAD_REQUEST


def handle_unexpected_error(e):
    return jsonify({"message": e.message}), HTTPStatus.INTERNAL_SERVER_ERROR