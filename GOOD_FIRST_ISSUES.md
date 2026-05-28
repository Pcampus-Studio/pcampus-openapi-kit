# Good First Issues

Welcome to `pcampus-openapi-kit`. These tasks are good entry points for new contributors.

Pick one, comment on the related GitHub issue, and open a pull request when ready.

## Documentation

- [ ] Add a Laravel quickstart mirroring `examples/fastapi/`
- [ ] Add a short "Why Pcampus OpenAPI?" blog-style doc in `docs/`
- [ ] Improve Thai/English bilingual quickstart examples

## Specs

- [ ] Flesh out `specs/auth/openapi.yaml` with token and `/auth/me` endpoints
- [ ] Add CRM customer CRUD to `specs/crm/openapi.yaml`
- [ ] Add notification subscription endpoints to `specs/notifications/openapi.yaml`
- [ ] Add inventory stock adjustment endpoints to `specs/inventory/openapi.yaml`

## Tooling

- [ ] Add a Spectral rule requiring 4xx responses to reference `ErrorResponse`
- [ ] Add a breaking-change checker script under `tooling/validation/`
- [ ] Add TypeScript SDK generation script under `tooling/generation/`

## Examples

- [ ] Add contract tests that validate FastAPI responses against the billing spec
- [ ] Add an AI agent read-only discovery script in `examples/ai-agent/`
- [ ] Add Node.js Express example for billing invoices

## Community

- [ ] Translate `docs/quickstart.md` to Thai
- [ ] Add more issue labels and CONTRIBUTING diagrams
- [ ] Create a release checklist document

## Before You Start

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Run `npm install && npm test`
3. Run `pytest examples/fastapi/tests -q` if you touch the example app

## Pull Request Expectations

- One focused change per PR
- Spec changes must pass `npm run lint` and `npm run validate`
- Include examples when adding new conventions or schemas
