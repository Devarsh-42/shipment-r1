from datetime import datetime
import uuid

class Plans:
    def __init__(self,store_location,valid_from,valid_to, items):
        self.id = str(uuid.uuid()),
        self.store_location = store_location
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.items: items

    def to_dict(self):
        return {
                "store_location": "Delhi",
                "valid_from": "2025-08-01",
                "valid_to": "2025-08-31",
                "items": [
                    {
                        "category": "veggie",
                        "name": "Tomato",
                        "half_price": 14,
                        "full_price": 27,
                        "extra_charge": 15
                    }
                ]
            }
    
    @staticmethod
    def from_dict(data):
        plans = Plans(
            store_location=data.get("store_location"),
            valid_from=data.get("valid_from"),
            valid_to = data.get("valid_to"),
            items = data.get("items")

        )

                            
                        
                
        
