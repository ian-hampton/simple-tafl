from flask import Blueprint, request, jsonify

from app.core import board
from app.core import validation

api_bp = Blueprint("api", __name__)

@api_bp.route("/state", methods=["GET"])
def state():
    board_state = board.get_board_state()
    data = {
        "state": board_state
    }
    return jsonify(data)

@api_bp.route("/moves", methods=["POST"])
def moves():
    data = request.get_json()
    location = data.get("move")

    id = board.location_to_id(location)
    legal_moves = validation.get_legal_moves(id)

    legal_moves_final = []
    for id in legal_moves:
        legal_moves_final.append(board.id_to_location(id))

    data = {
        "moves": legal_moves_final
    }

    return jsonify(data)