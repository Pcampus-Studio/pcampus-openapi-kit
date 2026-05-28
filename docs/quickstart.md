# Quickstart

Get from zero to a validated OpenAPI contract in about 15 minutes.

## 1. Clone and install

```bash
git clone https://github.com/pcampus-studio/pcampus-openapi-kit.git
cd pcampus-openapi-kit
npm install
```

## 2. Explore the reference billing module

The billing module is the canonical example of a production-ready domain spec:

```bash
cat specs/billing/openapi.yaml
```

It demonstrates:

- shared error and pagination `$ref`s
- explicit operation descriptions
- `x-agent-hints` on every endpoint
- deterministic status codes and examples

## 3. Lint and validate

```bash
npm run lint
npm run validate
```

Or target one file:

```bash
npx pcampus-openapi-kit lint specs/billing/openapi.yaml
npx pcampus-openapi-kit validate specs/billing/openapi.yaml
```

## 4. Scaffold your own API

Create a new CRUD spec from a template:

```bash
npx pcampus-openapi-kit init crud --name customer --out ./customers-api
npx pcampus-openapi-kit lint ./customers-api/openapi.yaml
npx pcampus-openapi-kit validate ./customers-api/openapi.yaml
```

Available templates:

| Template | Use case |
|----------|----------|
| `crud` | Tenant-scoped resource CRUD |
| `auth` | Token-based auth service |
| `webhook` | Webhook subscriptions |
| `event` | Event ingestion |

## 5. Run the reference implementation

```bash
cd examples/fastapi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
pytest -q
```

Visit http://127.0.0.1:8080/docs to inspect the billing API.

## 6. Start a mock server from the spec

From the repository root:

```bash
bash tooling/generation/mock-server.sh specs/billing/openapi.yaml
```

Prism serves mock responses at http://127.0.0.1:4010.

## 7. Adopt in your own repository

Copy these into your service repo:

```text
specs/shared/errors.yaml
specs/shared/pagination.yaml
conventions/
tooling/lint/
```

Or install the CLI and run it in CI:

```yaml
- run: npm install @pcampus/openapi-kit
- run: npx pcampus-openapi-kit lint ./openapi.yaml
- run: npx pcampus-openapi-kit validate ./openapi.yaml
```

## 8. Contribute back

Read:

- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [GOOD_FIRST_ISSUES.md](../GOOD_FIRST_ISSUES.md)
- [ROADMAP.md](../ROADMAP.md)

Then open a pull request with a focused spec, rule, or example improvement.

## Next steps

- [Workflows](workflows.md)
- [Human review checklist](human-review.md)
- [Agent consumption guide](agent-consumption.md)
