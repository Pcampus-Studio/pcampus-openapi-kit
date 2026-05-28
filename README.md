# pcampus-openapi-kit

Production-ready OpenAPI conventions and templates  
for Human + AI software teams.

[![CI](https://github.com/pcampus-studio/pcampus-openapi-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/pcampus-studio/pcampus-openapi-kit/actions/workflows/ci.yml)

**Version 1.0.0** — ready to use today.

---

## Quick Start

```bash
git clone https://github.com/pcampus-studio/pcampus-openapi-kit.git
cd pcampus-openapi-kit
npm install
npm test
```

Scaffold a new API:

```bash
npx pcampus-openapi-kit init crud --name customer --out ./customers-api
```

Run the billing reference app:

```bash
cd examples/fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
pytest -q
```

Full guide: [docs/quickstart.md](docs/quickstart.md)

---

## Overview

`pcampus-openapi-kit` is an opinionated OpenAPI-first toolkit designed for modern software teams building with both humans and AI agents.

This project focuses on:

- reusable API contracts
- deterministic schemas
- AI-readable specifications
- production-grade conventions
- spec-first workflows
- Human + AI collaboration

---

## Why This Exists

Most OpenAPI specifications today are written only for:

- documentation
- SDK generation
- API visualization

But modern systems are increasingly consumed by:

- AI coding assistants
- AI agents
- automation workflows
- code generators
- orchestration systems
- testing pipelines

Traditional API specs are often:

- inconsistent
- ambiguous
- difficult for AI to reason about
- hard to scale across teams

This project aims to solve that.

---

## Vision

We believe OpenAPI should become:

> The single source of truth for Human + AI software delivery.

Instead of:

```text
code → docs
```

We promote:

```text
spec → implementation → tests → SDKs → automation
```

---

## Core Principles

### 1. Contract First

Specifications define behavior before implementation.

The spec is the source of truth.

---

### 2. AI Readable

Descriptions should be explicit and deterministic.

Bad:

```yaml
description: get user
```

Good:

```yaml
description: Retrieve active user profile by UUID.
Returns 404 when user does not exist.
Returns 403 when requester lacks tenant access.
```

---

### 3. Deterministic Responses

APIs should always provide:

- predictable status codes
- stable schemas
- structured errors
- explicit nullability
- consistent pagination

---

### 4. Human Governance

AI may assist implementation.

Humans approve contracts.

API contracts are business decisions.

---

## Repository Structure

```text
pcampus-openapi-kit/
├── specs/
│   ├── auth/
│   ├── billing/
│   ├── crm/
│   ├── inventory/
│   ├── notifications/
│   └── shared/
│
├── conventions/
│   ├── naming.md
│   ├── pagination.md
│   ├── errors.md
│   ├── auth.md
│   ├── versioning.md
│   └── ai-guidelines.md
│
├── templates/
│   ├── resource-crud.yaml
│   ├── auth-service.yaml
│   ├── webhook.yaml
│   └── event-driven.yaml
│
├── examples/
│   ├── laravel/
│   ├── fastapi/
│   ├── node/
│   └── ai-agent/
│
├── generated/
│   ├── sdk/
│   ├── mocks/
│   └── tests/
│
├── tooling/
│   ├── lint/
│   ├── validation/
│   └── generation/
│
└── docs/
    ├── quickstart.md
    ├── philosophy.md
    ├── workflows.md
    ├── human-review.md
    └── agent-consumption.md
```

---

## AI-Ready Extensions

This project introduces conventions optimized for AI-native workflows.

Example:

```yaml
x-agent-hints:
  safe_to_retry: true
  destructive: false
  requires_confirmation: true
```

Possible metadata:

- retry safety
- destructive operations
- workflow hints
- next-step suggestions
- approval requirements

---

## Standard Error Contract

```yaml
components:
  schemas:
    ErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: string
              example: CUSTOMER_NOT_FOUND

            message:
              type: string
              example: Customer does not exist.

            details:
              type: object
```

See `specs/shared/errors.yaml` for the canonical reusable schema.

---

## Workflow Philosophy

```text
DEFINE
→ DESIGN SPEC
→ REVIEW
→ IMPLEMENT
→ TEST
→ VALIDATE
→ SHIP
```

Humans define and approve.

AI accelerates execution.

---

## Contributing

We welcome contributors who care about:

- scalable API design
- AI-native engineering
- spec-first development
- deterministic contracts
- reusable production patterns

Before contributing, please read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md)
- [ROADMAP.md](ROADMAP.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [conventions/](conventions/)
- [docs/philosophy.md](docs/philosophy.md)

---

## Long-Term Goal

The goal of this project is not to create random Swagger examples.

The goal is to build:

> reusable API contracts for the next generation of Human + AI software teams.

---

## Maintained By

Pcampus Studio
