# pcampus-openapi-kit

Production-ready OpenAPI conventions
for Human + AI software teams.

---

## Why

Modern APIs are no longer consumed by humans alone.

Today, APIs are also used by:

* AI coding assistants
* automation workflows
* SDK generators
* testing systems
* AI agents

But most OpenAPI specs today are still:

* inconsistent
* ambiguous
* difficult for AI to reason about

`pcampus-openapi-kit` aims to solve that.

---

## Goals

* reusable API contracts
* deterministic schemas
* AI-readable specifications
* spec-first workflows
* production-grade conventions

---

## Core Philosophy

Instead of:

code → docs

We believe in:

spec → implementation → tests → automation

---

## Principles

* Contract-first development
* AI-readable descriptions
* Standardized error handling
* Predictable API behavior
* Human-approved governance

---

## Example

```yaml
x-agent-hints:
  safe_to_retry: true
  destructive: false
  requires_confirmation: true
```

---

## Repository Structure

* `specs/` → reusable API modules
* `templates/` → starter OpenAPI templates
* `conventions/` → API standards
* `examples/` → framework examples
* `tooling/` → validation & generation tools

---

## Long-Term Vision

Build reusable API contracts
for the next generation of Human + AI software teams.

---

Maintained by Pcampus Studio
