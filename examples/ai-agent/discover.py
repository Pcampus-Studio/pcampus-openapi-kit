#!/usr/bin/env python3
"""Read-only discovery workflow for AI agents consuming pcampus-openapi-kit specs."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "specs" / "billing" / "openapi.yaml"


def load_spec() -> dict:
    with SPEC_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def discover(spec: dict) -> dict:
    paths = spec.get("paths", {})
    operations = []

    for path, methods in paths.items():
        for method, operation in methods.items():
            if method.startswith("x-"):
                continue

            hints = operation.get("x-agent-hints", {})
            operations.append(
                {
                    "method": method.upper(),
                    "path": path,
                    "operationId": operation.get("operationId"),
                    "safe_to_retry": hints.get("safe_to_retry"),
                    "destructive": hints.get("destructive"),
                    "requires_confirmation": hints.get("requires_confirmation"),
                    "workflow_hint": hints.get("workflow_hint"),
                }
            )

    return {
        "title": spec.get("info", {}).get("title"),
        "version": spec.get("info", {}).get("version"),
        "recommended_order": [
            op["operationId"]
            for op in operations
            if op["method"] == "GET" and not op["requires_confirmation"]
        ],
        "operations": operations,
    }


def main() -> int:
    if not SPEC_PATH.exists():
        print(f"Spec not found: {SPEC_PATH}", file=sys.stderr)
        return 1

    report = discover(load_spec())
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
