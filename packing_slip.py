import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/packing-slip",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "packing_slip_number": "PS-001",
        "date": "2026-03-15",
        "order_number": "ORD-4521",
        "shipping_method": "FedEx Ground",
        "tracking_number": "794644790132",
        "from": {
            "name": "Warehouse",
            "address": "500 Fulfillment Way\nPhoenix, AZ 85001",
        },
        "to": {
            "name": "Sarah Johnson",
            "address": "742 Evergreen Terrace\nSpringfield, IL 62704",
        },
        "items": [
            {"description": "Blue T-Shirt (L)", "quantity": 2, "sku": "BLU-TSH-L", "weight": "0.3 kg"},
            {"description": "Running Shoes", "quantity": 1, "sku": "RUN-SHO-42", "weight": "0.8 kg"},
        ],
        "notes": "Handle with care.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("packing-slip.pdf", "wb") as f:
    f.write(response.content)
print("Packing slip saved to packing-slip.pdf")
