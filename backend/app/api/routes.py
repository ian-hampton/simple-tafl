from flask import Blueprint, request, abort

from app.core import board
from app.core import state
from app.core import validation
from app.core import move

api_bp = Blueprint("api", __name__)

@api_bp.route("/state", methods=["GET"])
def game_state():
    data = {
        "board": board.get_board_state(),
        "turn": state.get_game_state()
    }
    return data

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
    
    return data

@api_bp.route("/move", methods=["POST"])
def resolve_move():
    data = request.get_json()
    start = data.get("start")
    dest = data.get("end")

    start_id = board.location_to_id(start)
    dest_id = board.location_to_id(dest)

    # reject move if it is invalid - should not occur just in case
    legal_moves = validation.get_legal_moves(start_id)
    if dest_id not in legal_moves:
        abort(422)

    # resolve move
    move.resolve(start_id, dest_id)

    return {}, 200