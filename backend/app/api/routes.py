from flask import Blueprint, jsonify

from app.services import board

api_bp = Blueprint("api", __name__)

@api_bp.route("/state", methods=["GET"])
def state():
    board_state = board.get_board_state()
    data = {
        "state": board_state
    }
    return jsonify(data)