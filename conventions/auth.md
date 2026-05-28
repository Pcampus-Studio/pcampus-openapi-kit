# Auth Conventions

## Security Schemes

Define auth once in shared specs and reference it from domain modules.

Supported patterns:

- Bearer JWT for user and service tokens
- API keys for machine-to-machine integrations
- OAuth2 authorization code for third-party clients

## Required Metadata

Every protected operation must document:

- required scopes or roles
- tenant isolation behavior
- whether the endpoint is safe for automation agents

## Example

```yaml
security:
  - bearerAuth: []

x-agent-hints:
  requires_confirmation: false
  destructive: false
```

## Token Claims

Document expected JWT claims in the auth module spec, not per endpoint.

Common claims:

- `sub`
- `tenant_id`
- `roles`
- `scopes`

## Failure Behavior

| Case | Status | Error Code |
|------|--------|------------|
| Missing token | 401 | `UNAUTHENTICATED` |
| Invalid token | 401 | `INVALID_TOKEN` |
| Valid token, insufficient access | 403 | `FORBIDDEN` |
| Valid token, wrong tenant | 403 | `TENANT_ACCESS_DENIED` |

## Agent Safety

Mark destructive or privileged operations explicitly:

```yaml
x-agent-hints:
  requires_confirmation: true
  destructive: true
```
