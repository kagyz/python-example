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
        "currency": "SAR",
        "direction": "rtl",
        "from": {
            "name": "شركة أكمي للتقنية",
            "email": "billing@acme-tech.sa",
            "address": "شارع الملك فهد\nالرياض 12345",
        },
        "to": {"name": "شركة التقدم للحلول", "email": "accounts@taqadum.sa"},
        "items": [
            {"description": "تصميم وتطوير الموقع الإلكتروني", "quantity": 1, "unit_price": 15000},
            {"description": "صيانة شهرية ودعم فني", "quantity": 6, "unit_price": 2000},
        ],
        "tax": {"rate": 15},
        "notes": "يرجى السداد خلال 30 يوماً من تاريخ الفاتورة.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("arabic-invoice.pdf", "wb") as f:
    f.write(response.content)
print("Arabic invoice saved to arabic-invoice.pdf")
