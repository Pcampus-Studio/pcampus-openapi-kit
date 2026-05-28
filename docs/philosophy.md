# Philosophy

`pcampus-openapi-kit` treats OpenAPI as a delivery contract, not a documentation afterthought.

## Spec First

Behavior is defined in the specification before code is written.
Implementation, tests, SDKs, and automation all derive from the same source of truth.

## Deterministic By Design

Ambiguity creates bugs for humans and incorrect actions for AI agents.
Every contract should make success and failure paths explicit.

## Human Governance, AI Acceleration

Humans own business decisions and approve API contracts.
AI tools accelerate drafting, implementation, testing, and refactors around approved specs.

## Reuse Over Reinvention

Shared schemas, error models, auth patterns, and templates reduce drift across teams and services.

## Production Orientation

Conventions in this repository prioritize operability:

- predictable status codes
- structured errors
- explicit nullability
- stable pagination
- agent-safe metadata

The goal is not prettier Swagger files.
The goal is reliable collaboration between humans and AI systems at scale.
