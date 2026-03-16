import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/credit-note",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "credit_note_number": "CN-001",
        "date": "2026-03-15",
        "currency": "USD",
        "invoice_number": "INV-001",
        "reason": "Overcharge correction",
        "from": {"name": "Acme Corp"},
        "to": {"name": "Client Inc."},
        "items": [
            {"description": "Billing adjustment", "quantity": 1, "unit_price": 500}
        ],
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("credit-note.pdf", "wb") as f:
    f.write(response.content)
print("Credit note saved to credit-note.pdf")
