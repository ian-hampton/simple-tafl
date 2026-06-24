from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/state", methods=["GET"])
def state():
    board_state = "N/A"
    data = {
        "state": board_state
    }
    return jsonify(data)