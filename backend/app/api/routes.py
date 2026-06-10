from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Successfully connected to Flask backend."})