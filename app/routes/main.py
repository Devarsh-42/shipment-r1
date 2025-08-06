from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({
        "message": "Shipments API is running",
        "status": "ok",
        "endpoints": {
            "health": "/health",
            "shipments": "/api/shipments"
        }
    })