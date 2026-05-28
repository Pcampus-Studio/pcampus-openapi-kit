# Error Conventions

All APIs in this kit use a single structured error contract.

## Canonical Schema

See `specs/shared/errors.yaml`.

## Response Shape

```json
{
  "error": {
    "code": "CUSTOMER_NOT_FOUND",
    "message": "Customer does not exist.",
    "details": {}
  }
}
```

## Rules

1. Use machine-readable `code` values in SCREAMING_SNAKE_CASE.
2. Use human-readable `message` values suitable for logs and UI.
3. Put field-level validation issues in `details`.
4. Never return unstructured plain-text errors for client-facing endpoints.
5. Document every non-2xx response in the OpenAPI operation.

## Status Code Guidance

| Status | Use When |
|--------|----------|
| 400 | Request is malformed or fails validation |
| 401 | Authentication is missing or invalid |
| 403 | Authenticated but not authorized |
| 404 | Resource does not exist or is not visible |
| 409 | Conflict with current resource state |
| 422 | Semantically invalid but well-formed input |
| 429 | Rate limit exceeded |
| 500 | Unexpected server failure |

## Example Operation Response

```yaml
'404':
  description: Customer does not exist for the given ID.
  content:
    application/json:
      schema:
        $ref: '../shared/errors.yaml#/components/schemas/ErrorResponse'
      example:
        error:
          code: CUSTOMER_NOT_FOUND
          message: Customer does not exist.
