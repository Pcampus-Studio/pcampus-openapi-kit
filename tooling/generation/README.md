# Generation Tooling

Scripts for generating mocks and future SDK artifacts from approved specs.

## Mock server

Requires Node.js 18+.

```bash
bash tooling/generation/mock-server.sh specs/billing/openapi.yaml
```

This starts a Prism mock server at `http://127.0.0.1:4010`.

Stop it with:

```bash
kill "$(cat generated/mocks/prism.pid)"
```

## Planned outputs

- client SDKs under `generated/sdk/`
- contract tests under `generated/tests/`

Generated artifacts are not committed to source control.
