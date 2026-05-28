# Workflows

Recommended delivery flow for teams using this kit.

## 1. Define

Capture the business capability, actors, and constraints.
Identify whether the change is net-new or an extension of an existing module.

## 2. Design Spec

Draft or update OpenAPI modules under `specs/`.
Reuse shared components from `specs/shared/` whenever possible.

## 3. Review

Human reviewers validate:

- naming consistency
- auth and tenancy rules
- error behavior
- pagination strategy
- agent hints for sensitive operations

## 4. Implement

Generate or hand-write server code from the approved spec.
Framework examples live under `examples/`.

## 5. Test

Validate responses against the spec using contract tests and mocked fixtures.
Generated test scaffolding may be placed under `generated/tests/`.

## 6. Validate

Run linting and validation tooling under `tooling/`.
Reject drift between implementation and spec.

## 7. Ship

Publish SDKs, mocks, and docs from the same approved contract.
Track breaking changes through versioning conventions.

## Working With AI Agents

Agents may:

- draft specs from requirements
- implement handlers from approved operations
- generate tests and client stubs
- propose refactors that preserve contract behavior

Agents should not:

- merge breaking contract changes without human approval
- invent undocumented status codes or error shapes
- omit nullability or response descriptions
