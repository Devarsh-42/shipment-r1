from datetime import datetime
from app.models.store import Store
from bson import ObjectId


class PlansServices:
    def __init__(self,db):
        db= self.db
        self.collection = db.stores

    def create_plane(self,data):
        plan = plan(
            plan_location=data["plan_location"],
            currency=data["currency"],
            tax_percentage=data["tax_percentage"],
            premium_items=data["premium_items"]
        )

        plan_dict = plan.to_dict()
        result = self.collection.insert_one(plan_dict)
        plan_dict['id'] = str(result.inserted_id)
        return plan_dict
    
    def get_all_plan(self, status_filter=None):
        query = {}
        if status_filter:
            query['status'] = status_filter
        
        plan = []
        for doc in self.collection.find(query):
            doc['_id'] = str(doc['_id'])
            plan.append(doc)
        return plan
    
    def get_shipment_by_id(self, order_id):
        """Get a single plan by orderId"""
        plan = self.collection.find_one({"orderId": order_id})
        if plan:
            plan['_id'] = str(plan['_id'])
            return plan
        return None
    
    def update_plan_status(self, order_id, status):
        """Update plan status"""
        result = self.collection.update_one(
            {"orderId": order_id},
            {
                "$set": {
                    "status": status,
                    "updatedAt": datetime.utcnow().isoformat()
                }
            }
        )
        
        if result.matched_count > 0:
            return self.get_plan_by_id(order_id)
        return None



