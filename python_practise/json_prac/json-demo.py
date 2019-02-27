import json
from pprint import pprint

customer_data = {
    "customers": [
        {"id": 525, "name": "robin sharma", "address": "nagpur"},
        {"id": 526, "name": "alex pandian", "address": "chennai"},
        {"id": 527, "name": "saurabh mishra", "address": "kolkata"},
    ],
    "profits": None,
    "market-share": True
}

data = json.dumps(customer_data, indent=2, sort_keys=False)

with open('customers.json_prac', 'w') as f:
    f.write(data)
