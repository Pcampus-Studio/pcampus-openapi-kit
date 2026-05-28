# Validation Tooling

OpenAPI structural validation with reference resolution.

## Run locally

```bash
npm install
npm run validate
```

Validate a specific module:

```bash
npx pcampus-openapi-kit validate specs/billing/openapi.yaml
```

Validation uses `@apidevtools/swagger-parser` to resolve `$ref` links across `specs/shared/`.

## CI

GitHub Actions runs `npm test` (lint + validate) on every pull request.

## Consumer projects

Use the composite action:

```yaml
- uses: pcampus-studio/pcampus-openapi-kit/.github/actions/validate@v1
  with:
    spec: ./openapi.yaml
```
