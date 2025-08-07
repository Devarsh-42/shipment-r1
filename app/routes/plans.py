from flask import Blueprint, request, jsonify, current_app
from app.services.plans import PlansServices

plans_bp = Blueprint('plans', __name__, url_prefix='/api/plans')

def get_plans_service():
    return PlansServices(current_app.db)

@plans_bp.route('/create-plans', methods=['POST'])
def create_plans():
    try:
        data = request.get_json()
        
        # Create shipment
        service = get_plans_service()
        shipment = service.create_plans(data)
        
        return jsonify(shipment), 201
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@plans_bp.route('/get-plans', methods=['GET'])
def get_all_planss():
    try:
        status_filter = request.args.get('status')
        
        service = get_plans_service()
        shipments = service.get_all_shipments(status_filter)
        
        return jsonify(shipments), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@plans_bp.route('/<plans_id>', methods=['GET'])
def get_shipment(order_id):
    """Get a single plans order by ID"""
    try:
        service = get_plans_service()
        shipment = service.get_shipment_by_id(order_id)
        
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404
        
        return jsonify(shipment), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@plans_bp.route('/<plans_id>', methods=['PATCH'])
def update_plans_status(order_id):
    """Update plans status"""
    try:
        data = request.get_json()
        
        service = get_plans_service()
        shipment = service.update_plans_status(order_id, data['status'])
        
        if not shipment:
            return jsonify({"error": "plans not found"}), 404
        
        return jsonify(shipment), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@plans_bp.route('/<plans_id>', methods=['DELETE'])
def delete_shipment(plans_id):
    """Delete a shipment order"""
    try:
        service = get_plans_service()
        deleted = service.delete_shipment(plans_id)
        
        if not deleted:
            return jsonify({"error": "plans not found"}), 404
        
        return '', 204
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500