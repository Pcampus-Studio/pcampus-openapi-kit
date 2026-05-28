from __future__ import annotations

from datetime import date, datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class InvoiceStatus(str, Enum):
    draft = "draft"
    open = "open"
    paid = "paid"
    void = "void"


class InvoiceLineItem(BaseModel):
    description: str
    quantity: int = Field(ge=1)
    unit_amount: float = Field(ge=0)


class InvoiceCreateRequest(BaseModel):
    customer_id: UUID
    invoice_number: str
    currency: str = Field(min_length=3, max_length=3)
    due_date: date | None = None
    line_items: list[InvoiceLineItem] = Field(min_length=1)


class InvoiceUpdateRequest(BaseModel):
    due_date: date | None = None
    line_items: list[InvoiceLineItem] | None = Field(default=None, min_length=1)
    status: InvoiceStatus | None = None


class Invoice(BaseModel):
    id: UUID
    customer_id: UUID
    invoice_number: str
    status: InvoiceStatus
    currency: str
    amount_due: float
    due_date: date | None
    line_items: list[InvoiceLineItem]
    created_at: datetime
    updated_at: datetime


class PaginationMeta(BaseModel):
    next_cursor: str | None = None
    has_more: bool
    limit: int


class PaginatedInvoiceList(BaseModel):
    data: list[Invoice]
    pagination: PaginationMeta


class ErrorBody(BaseModel):
    code: str
    message: str
    details: dict[str, Any] | None = None


class ErrorResponse(BaseModel):
    error: ErrorBody


def calculate_amount_due(line_items: list[InvoiceLineItem]) -> float:
    return round(sum(item.quantity * item.unit_amount for item in line_items), 2)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
