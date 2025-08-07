from datetime import datetime
import uuid

class Store:
    def __init__(self,store_location, currency, tax_percentage, premium_items):
        self.id = str(uuid.uuid()),
        self.store_location = store_location
        self.currency = currency
        self.tax_percentage = tax_percentage
        self.premium_items = premium_items

    def to_dict(self):
        return {
                    "store_location": "Delhi",
                    "currency": "INR",
                    "tax_percentage": 6.0,
                    "premium_items": ["Tomato", "Paneer Tikka"]
                }
    
    @staticmethod
    def from_dict(data):
        store = Store(
            store_location=data["store_location"],
            currency=data["currency"],
            tax_percentage=data["tax_percentage"],
            premium_items=data["premium_items"]
        )
        if 'store_id' in data: store.store_location = data["store_id"],


    

