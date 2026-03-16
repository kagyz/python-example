import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/invoice",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "invoice_number": "INV-001",
        "issue_date": "2026-03-15",
        "due_date": "2026-04-15",
        "currency": "USD",
        "from": {
            "name": "Acme Corp",
            "email": "billing@acme.com",
            "address": "123 Main St\nNew York, NY 10001",
        },
        "to": {"name": "Client Inc.", "email": "accounts@client.com"},
        "items": [
            {"description": "Web Development", "quantity": 40, "unit_price": 150},
            {"description": "Design Review", "quantity": 5, "unit_price": 200},
        ],
        "tax": {"rate": 8.25},
        "notes": "Payment due within 30 days.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("invoice.pdf", "wb") as f:
    f.write(response.content)
print("Invoice saved to invoice.pdf")
