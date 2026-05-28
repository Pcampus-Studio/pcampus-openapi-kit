# Pagination Conventions

## Cursor-Based Pagination (Preferred)

Use cursor pagination for large or frequently changing collections.

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cursor` | string | Opaque cursor from a previous response |
| `limit` | integer | Maximum items to return (default: 20, max: 100) |

### Response Shape

```yaml
PaginatedList:
  type: object
  required:
    - data
    - pagination
  properties:
    data:
      type: array
      items:
        $ref: '#/components/schemas/Resource'
    pagination:
      type: object
      required:
        - has_more
      properties:
        next_cursor:
          type: string
          nullable: true
          description: Present when has_more is true.
        has_more:
          type: boolean
        limit:
          type: integer
```

## Offset Pagination (Limited Use)

Use only for admin tools or stable, small datasets.

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | 1-based page number |
| `per_page` | integer | Items per page (default: 20, max: 100) |

Always document performance implications in the operation description.

## Sorting

Use explicit sort fields:

```text
?sort=created_at
?sort=-created_at
```

Document allowed sort fields in the operation description.
