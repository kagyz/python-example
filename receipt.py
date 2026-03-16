import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/receipt",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "receipt_number": "REC-001",
        "date": "2026-03-15",
        "currency": "USD",
        "payment_method": "Credit Card",
        "transaction_id": "txn_1234567890",
        "from": {"name": "Acme Corp"},
        "to": {"name": "John Doe", "email": "john@example.com"},
        "items": [
            {"description": "Pro Plan — Monthly", "quantity": 1, "unit_price": 49}
        ],
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("receipt.pdf", "wb") as f:
    f.write(response.content)
print("Receipt saved to receipt.pdf")
