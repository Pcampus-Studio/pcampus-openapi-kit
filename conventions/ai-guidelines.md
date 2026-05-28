# AI Guidelines

These conventions help AI agents consume OpenAPI specs safely and deterministically.

## Write Specs For Reasoning, Not Decoration

Descriptions must answer:

- What does this operation do?
- What inputs are required?
- What failures can occur?
- Is the operation safe to retry?
- Does it mutate state?

## Required Extensions

Use `x-agent-hints` on operations that agents may invoke:

```yaml
x-agent-hints:
  safe_to_retry: true
  destructive: false
  requires_confirmation: true
  workflow_hint: "Fetch customer before creating an invoice."
```

## Field Nullability

Always declare nullable fields explicitly. Agents should not infer nullability from examples alone.

## Enum Stability

Prefer string enums with stable values. Document whether unknown enum values should be ignored or rejected.

## Pagination And Discovery

Document list endpoints with:

- default limits
- sorting options
- filter semantics
- whether results are tenant-scoped

## Error Interpretation

Agents must treat `error.code` as the primary branch key.
Use consistent codes across services for the same failure mode.

## Human Approval Boundary

Agents may propose spec changes and implementations.
Humans approve contract changes before merge.

See also:

- [docs/agent-consumption.md](../docs/agent-consumption.md)
- [docs/human-review.md](../docs/human-review.md)
