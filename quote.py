import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/quote",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "quote_number": "QUO-001",
        "date": "2026-03-15",
        "currency": "USD",
        "title": "Estimate",
        "expiry_date": "2026-04-15",
        "from": {"name": "Design Studio"},
        "to": {"name": "Startup Inc."},
        "items": [
            {"description": "Logo Design", "quantity": 1, "unit_price": 2000},
            {"description": "Brand Guidelines", "quantity": 1, "unit_price": 3500},
        ],
        "notes": "Valid for 30 days. 50% deposit required to begin.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("quote.pdf", "wb") as f:
    f.write(response.content)
print("Quote saved to quote.pdf")
