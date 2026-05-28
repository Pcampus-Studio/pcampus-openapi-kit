# Naming Conventions

## Paths

Use kebab-case for URL paths.

```text
/users/{user_id}/orders
/billing/invoices/{invoice_id}
```

## Operation IDs

Use `{resource}_{action}` in snake_case.

```yaml
operationId: list_users
operationId: get_user
operationId: create_user
operationId: update_user
operationId: delete_user
```

## Schema Names

Use PascalCase for reusable schema names.

```yaml
User
UserCreateRequest
UserUpdateRequest
PaginatedUserList
ErrorResponse
```

## Fields

Use snake_case for JSON property names unless a downstream standard requires otherwise.

```yaml
user_id:
created_at:
tenant_id:
```

## Tags

Group endpoints by bounded context or domain module.

```yaml
tags:
  - Users
  - Billing
  - Auth
```

## Descriptions

Every operation, parameter, and response must include a description that states:

- what the operation does
- important preconditions
- notable status codes and when they occur

Avoid vague verbs like "get", "handle", or "process" without context.
