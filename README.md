# Kagyz Python Examples

Generate professional PDF documents from JSON using the [Kagyz API](https://kagyz.com). Each script demonstrates a different document type.

## Quick Start

```bash
git clone https://github.com/kagyz/python-example.git
cd python-example
pip install -r requirements.txt
cp .env.example .env
```

Add your API key to `.env`:

```
KAGYZ_API_KEY=your_api_key_here
```

Get your API key at [kagyz.com](https://kagyz.com).

## Examples

| Script | Command | Description |
|--------|---------|-------------|
| `invoice.py` | `python invoice.py` | Standard invoice with tax |
| `receipt.py` | `python receipt.py` | Payment receipt with transaction ID |
| `quote.py` | `python quote.py` | Quote / estimate with expiry date |
| `credit_note.py` | `python credit_note.py` | Credit note referencing an invoice |
| `packing_slip.py` | `python packing_slip.py` | Packing slip with SKUs and weights |
| `arabic_invoice.py` | `python arabic_invoice.py` | RTL Arabic invoice (SAR currency) |
| `branded_invoice.py` | `python branded_invoice.py` | Invoice with custom accent color |

## Custom Branding

You can override the accent color per-request using the `branding` field:

```python
"branding": {
    "accent_color": "#22c55e"
}
```

To add your company logo, upload it via the [Kagyz Dashboard](https://app.kagyz.com/branding). The logo will appear on all generated documents automatically.

## How It Works

Each script sends a JSON payload to the Kagyz API and saves the returned PDF:

```python
response = requests.post(
    "https://api.kagyz.com/v1/invoice",
    headers={
        "Authorization": f"Bearer {os.getenv('KAGYZ_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "invoice_number": "INV-001",
        "currency": "USD",
        # ... your data
    },
)

with open("invoice.pdf", "wb") as f:
    f.write(response.content)
```

## Requirements

- Python 3.7+
- A Kagyz API key

## Links

- [Kagyz Documentation](https://kagyz.com/docs)
- [API Reference](https://kagyz.com/docs/api)
- [Node.js Examples](https://github.com/kagyz/node-example)

## License

MIT
