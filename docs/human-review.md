# Human Review

API contracts are business decisions. Human review is required before merge.

## Review Checklist

### Contract Clarity

- [ ] Operation descriptions state purpose and failure modes
- [ ] Request and response schemas are complete
- [ ] Nullability is explicit
- [ ] Examples match the schema

### Consistency

- [ ] Naming follows [conventions/naming.md](../conventions/naming.md)
- [ ] Errors use [specs/shared/errors.yaml](../specs/shared/errors.yaml)
- [ ] Pagination follows [conventions/pagination.md](../conventions/pagination.md)
- [ ] Auth behavior follows [conventions/auth.md](../conventions/auth.md)

### Safety

- [ ] Destructive operations include `x-agent-hints`
- [ ] Authorization requirements are documented
- [ ] Tenant scoping is explicit for multi-tenant resources

### Versioning

- [ ] Breaking changes bump major version or are rejected
- [ ] Deprecations include migration guidance

## Approval Model

1. Author opens a pull request with spec changes.
2. Reviewer validates against this checklist.
3. A maintainer approves and merges.
4. Implementation work may proceed in parallel only after contract approval.

## When To Escalate

Escalate review when a change affects:

- authentication or authorization models
- billing or payment flows
- personally identifiable information handling
- cross-service shared schemas
