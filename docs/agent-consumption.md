# Agent Consumption

This document describes how AI agents should read and act on specs from this repository.

## Priority Order

When interpreting an operation, agents should read in this order:

1. `operationId`
2. `description`
3. request body and parameter schemas
4. documented responses and error codes
5. `x-agent-hints`
6. examples

## Decision Rules

### Retry Safety

If `x-agent-hints.safe_to_retry` is `true`, agents may retry transient failures such as network timeouts or 503 responses.

If `false` or absent on a mutating operation, agents must not blindly retry.

### Confirmation

If `requires_confirmation` is `true`, agents must obtain explicit human confirmation before invoking the operation.

### Destructive Operations

If `destructive` is `true`, agents must explain the impact before execution and prefer dry-run or read-only discovery steps when available.

## Error Handling

Agents should branch on `error.code`, not HTTP status alone.

Example:

```json
{
  "error": {
    "code": "CUSTOMER_NOT_FOUND",
    "message": "Customer does not exist."
  }
}
```

Recommended behavior:

- `404` + `CUSTOMER_NOT_FOUND` → stop and report missing entity
- `403` + `TENANT_ACCESS_DENIED` → stop and request correct tenant context
- `400` with field details → repair input and retry once if safe

## Discovery Pattern

For unfamiliar domains, agents should:

1. read shared schemas
2. list collection endpoints
3. fetch a single resource
4. only then perform mutating actions

## Spec Changes

Agents may propose spec edits, but humans approve merges.
Do not treat generated implementation code as the source of truth over the OpenAPI file.
