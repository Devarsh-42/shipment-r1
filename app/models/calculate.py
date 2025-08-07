from datetime import datetime
import uuid

class Calculate:
    def __init__(self,store_location, order_date, length, selections, extras):
        self.id = str(uuid.uuid()),
        self.store_location = store_location
        self.order_date = order_date
        self.length = length
        self.selections = selections
        self.extras = extras

    def to_dict(self):
        return {
                    "store_location": "Mumbai",
                    "order_date": "2025-07-10",
                    "length": "full",
                    "selections": {
                        "bread": ["Italian"],
                        "sauce": ["Mayo", "BBQ"],
                        "veggie": ["Lettuce", "Tomato"]
                    },
                    "extras": {
                        "sauce": ["Mayo"],
                        "veggie": ["Tomato","Lettuce"]
                    }
                }
    @staticmethod
    def from_dict(data):
        calculate = Calculate(
            store_location=data['store_location']
        )
        
        

        

    

