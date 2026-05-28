from __future__ import annotations

from pathlib import Path

import yaml
from fastapi import FastAPI

from app.routes.invoices import router as invoices_router

ROOT = Path(__file__).resolve().parents[3]
SPEC_PATH = ROOT / "specs" / "billing" / "openapi.yaml"

app = FastAPI(
    title="Billing API Example",
    version="1.0.0",
    description="Reference implementation of specs/billing/openapi.yaml",
)

app.include_router(invoices_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if SPEC_PATH.exists():
    with SPEC_PATH.open("r", encoding="utf-8") as handle:
        openapi_schema = yaml.safe_load(handle)

    app.openapi = lambda: openapi_schema
