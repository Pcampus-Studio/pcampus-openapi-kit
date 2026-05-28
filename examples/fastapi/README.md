# FastAPI Example

Reference implementation of [`specs/billing/openapi.yaml`](../../specs/billing/openapi.yaml).

This example shows how to:

- implement invoice endpoints from an approved OpenAPI contract
- return structured errors using the shared `ErrorResponse` shape
- expose the canonical OpenAPI document from the repository spec

## Requirements

- Python 3.11+
- Node.js 18+ (for repo-level lint/validate)

## Setup

```bash
cd examples/fastapi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the API

From `examples/fastapi`:

```bash
uvicorn app.main:app --reload --port 8080
```

Open:

- Health check: http://127.0.0.1:8080/health
- OpenAPI docs: http://127.0.0.1:8080/docs
- List invoices: http://127.0.0.1:8080/v1/invoices

## Run tests

```bash
pytest -q
```

## Validate the contract

From the repository root:

```bash
npm install
npm run lint
npm run validate
pytest examples/fastapi/tests -q
```

## Try the mock server

From the repository root:

```bash
bash tooling/generation/mock-server.sh specs/billing/openapi.yaml
```

Prism serves example responses from the spec at http://127.0.0.1:4010.
