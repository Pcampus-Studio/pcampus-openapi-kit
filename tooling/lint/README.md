# Lint Tooling

Spectral ruleset for `pcampus-openapi-kit` conventions.

## Run locally

```bash
npm install
npm run lint
```

Or lint a specific file:

```bash
npx pcampus-openapi-kit lint specs/billing/openapi.yaml
```

## Rules

Custom rules live in `rules/pcampus.js`:

- `pcampus-operation-id-snake-case` — operationId must be snake_case
- `pcampus-operation-description-min-length` — descriptions must be explicit
- `pcampus-mutation-agent-hints` — mutating operations require `x-agent-hints`
- `pcampus-agent-hints-shape` — agent hints must include retry/destructive/confirmation flags

## Use in your project

Copy `spectral.yaml` and `rules/` into your repository, or run this CLI against your specs after install:

```bash
npx @pcampus/openapi-kit lint ./openapi.yaml
```
