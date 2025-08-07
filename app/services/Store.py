from datetime import datetime
from bson import ObjectId

from app.models.store import Store


class StoreServices:
    def __init__(self,db):
        db= self.db
        self.collection = db.stores

    def create_store(self,data):
        store = Store(
            store_location=data["store_location"],
            currency=data["currency"],
            tax_percentage=data["tax_percentage"],
            premium_items=data["premium_items"]
        )

        store_dict = store.to_dict()
        result = self.collection.insert_one(store_dict)
        store_dict['id'] = str(result.inserted_id)
        return store_dict
    
    def get_all_store(self, status_filter=None):
        query = {}
        if status_filter:
            query['status'] = status_filter
        
        store = []
        for doc in self.collection.find(query):
            doc['_id'] = str(doc['_id'])
            store.append(doc)
        return store
    
    def get_shipment_by_id(self, order_id):
        """Get a single store by orderId"""
        store = self.collection.find_one({"orderId": order_id})
        if store:
            store['_id'] = str(store['_id'])
            return store
        return None
    
    def update_store_status(self, order_id, status):
        """Update store status"""
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
            return self.get_store_by_id(order_id)
        return None



