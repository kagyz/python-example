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
        "invoice_number": "INV-EMAIL-001",
        "issue_date": "2026-03-19",
        "due_date": "2026-04-19",
        "currency": "USD",
        "from": {
            "name": "Acme Corp",
            "email": "billing@acme.com",
            "address": "123 Main St\nNew York, NY 10001",
        },
        "to": {"name": "Client Inc.", "email": "client@example.com"},
        "items": [
            {"description": "Web Development", "quantity": 10, "unit_price": 150},
            {"description": "Design Review", "quantity": 5, "unit_price": 200},
        ],
        "tax": {"rate": 8.25},
        "deliver_to": {
            "email": "client@example.com",
            "subject": "Invoice INV-EMAIL-001 from Acme Corp",
            "message": "Hi,\n\nPlease find your invoice attached.\n\nThank you,\nAcme Corp",
        },
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

# PDF is still returned even when email is sent
delivered = response.headers.get("X-Kagyz-Delivered-To")
with open("email-invoice.pdf", "wb") as f:
    f.write(response.content)
print("Invoice saved to email-invoice.pdf")
if delivered:
    print(f"Invoice also emailed to: {delivered}")
