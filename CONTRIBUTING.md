# Contributing

Thank you for contributing to `pcampus-openapi-kit`.

## Quick Start For Contributors

```bash
git clone https://github.com/pcampus-studio/pcampus-openapi-kit.git
cd pcampus-openapi-kit
npm install
npm test
cd examples/fastapi && pip install -r requirements.txt && pytest -q
```

Read [docs/quickstart.md](docs/quickstart.md) for the full 15-minute onboarding flow.

## Before You Start

Read these resources in order:

1. [docs/philosophy.md](docs/philosophy.md)
2. [conventions/](conventions/)
3. [docs/workflows.md](docs/workflows.md)
4. [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## What We Accept

- Reusable OpenAPI modules under `specs/`
- Convention updates under `conventions/`
- Starter templates under `templates/`
- Framework examples under `examples/`
- Tooling improvements under `tooling/`

See [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md) for beginner-friendly tasks.

## Pull Request Guidelines

1. Keep changes focused on one concern.
2. Write explicit, deterministic descriptions in specs.
3. Follow existing naming and error conventions.
4. Include examples when introducing new patterns.
5. Do not commit generated artifacts under `generated/`.
6. Run `npm test` before opening a PR.
7. Run FastAPI tests when touching `examples/fastapi/`.

## Spec Changes Require Human Review

API contracts are business decisions. Spec changes should be reviewed by a human maintainer before merge.

Use the spec contribution issue template when proposing new domain modules.

## Project Structure

| Path | Purpose | Contribution bar |
|------|---------|------------------|
| `specs/shared/` | Cross-team reusable schemas | High review bar |
| `specs/<domain>/` | Domain modules | Medium review bar |
| `templates/` | Starter specs | Medium review bar |
| `tooling/lint/` | Spectral rules | Medium review bar |
| `examples/` | Reference implementations | Medium review bar |
| `conventions/` | Written standards | High review bar |

## Release Process

Maintainers cut releases from `main` using semantic versioning.
See [CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md).

## Questions

Open an issue for design discussions before large refactors or new domain modules.
