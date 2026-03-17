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
        "invoice_number": "INV-BRAND-001",
        "issue_date": "2026-03-17",
        "due_date": "2026-04-17",
        "currency": "USD",
        "branding": {
            "accent_color": "#22c55e"
        },
        "from": {
            "name": "Acme Corp",
            "email": "billing@acme.com",
            "address": "123 Main St\nNew York, NY 10001",
        },
        "to": {"name": "Client Inc.", "email": "accounts@client.com"},
        "items": [
            {"description": "Web Development", "quantity": 10, "unit_price": 150},
            {"description": "Design Review", "quantity": 5, "unit_price": 200},
        ],
        "tax": {"rate": 8.25},
        "notes": "Thank you for your business.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("branded-invoice.pdf", "wb") as f:
    f.write(response.content)
print("Branded invoice saved to branded-invoice.pdf")
