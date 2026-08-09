from flask import Blueprint, request, abort

from app.services import services

api_bp = Blueprint("api", __name__)

@api_bp.route("/state", methods=["GET"])
def game_state():
    return services.get_game_state()

@api_bp.route("/moves", methods=["POST"])
def moves():
    data = request.get_json()
    location = data.get("move")
    return services.get_legal_moves(location)

@api_bp.route("/move", methods=["POST"])
def resolve_move():
    data = request.get_json()
    start = data.get("start")
    dest = data.get("end")
    success = services.execute_move(start, dest)
    if not success:
        abort(422)
    return {}, 200