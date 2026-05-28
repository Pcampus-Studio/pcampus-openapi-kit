# Versioning Conventions

## URL Versioning (Default)

Use major version in the path:

```text
/v1/users
/v1/billing/invoices
```

Do not embed minor or patch versions in URLs.

## Breaking Changes

A breaking change requires a new major version.

Examples of breaking changes:

- removing a field
- changing field type or nullability
- changing status code behavior
- renaming paths or operation IDs used by clients

## Non-Breaking Changes

These may ship in the current major version:

- adding optional fields
- adding new endpoints
- adding new enum values when clients tolerate unknown values
- expanding descriptions

## Deprecation

Mark deprecated operations explicitly:

```yaml
deprecated: true
description: |
  Deprecated. Use GET /v1/users/{user_id}/profile instead.
  Will be removed in v2.
```

## Changelog Discipline

Document spec changes in pull requests and release notes.
Humans approve version bumps.
