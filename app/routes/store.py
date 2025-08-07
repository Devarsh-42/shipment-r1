from flask import Blueprint, request, jsonify, current_app
from app.services.Store import StoreServices

store_bp = Blueprint('store', __name__, url_prefix='/api/store')

def get_store_service():
    return StoreServices(current_app.db)

@store_bp.route('/create-store', methods=['POST'])
def create_store():
    try:
        data = request.get_json()
        
        # Create shipment
        service = get_store_service()
        shipment = service.create_store(data)
        
        return jsonify(shipment), 201
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@store_bp.route('/get-store', methods=['GET'])
def get_all_stores():
    try:
        status_filter = request.args.get('status')
        
        service = get_store_service()
        shipments = service.get_all_shipments(status_filter)
        
        return jsonify(shipments), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@store_bp.route('/<store_id>', methods=['GET'])
def get_shipment(order_id):
    """Get a single store order by ID"""
    try:
        service = get_store_service()
        shipment = service.get_shipment_by_id(order_id)
        
        if not shipment:
            return jsonify({"error": "Shipment not found"}), 404
        
        return jsonify(shipment), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@store_bp.route('/<store_id>', methods=['PATCH'])
def update_store_status(order_id):
    """Update store status"""
    try:
        data = request.get_json()
        
        service = get_store_service()
        shipment = service.update_store_status(order_id, data['status'])
        
        if not shipment:
            return jsonify({"error": "store not found"}), 404
        
        return jsonify(shipment), 200
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@store_bp.route('/<store_id>', methods=['DELETE'])
def delete_shipment(store_id):
    """Delete a shipment order"""
    try:
        service = get_store_service()
        deleted = service.delete_shipment(store_id)
        
        if not deleted:
            return jsonify({"error": "store not found"}), 404
        
        return '', 204
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500