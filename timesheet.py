import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.kagyz.com/v1/timesheet",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "timesheet_number": "TS-001",
        "date": "2026-03-17",
        "due_date": "2026-04-17",
        "currency": "USD",
        "period": "March 1–15, 2026",
        "hourly_rate": 150,
        "from": {"name": "Jane Smith", "email": "jane@freelancer.com"},
        "to": {"name": "TechCorp Inc.", "email": "accounts@techcorp.com"},
        "entries": [
            {"date": "2026-03-01", "description": "Frontend development", "hours": 8},
            {"date": "2026-03-02", "description": "API integration", "hours": 6.5},
            {"date": "2026-03-03", "description": "Code review", "hours": 4},
        ],
        "notes": "Payment due within 30 days.",
    },
)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

with open("timesheet.pdf", "wb") as f:
    f.write(response.content)
print("Timesheet saved to timesheet.pdf")
