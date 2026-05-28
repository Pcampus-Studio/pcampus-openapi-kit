from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Query, Response

from app.errors import error_response
from app.schemas import (
    Invoice,
    InvoiceCreateRequest,
    InvoiceStatus,
    InvoiceUpdateRequest,
    PaginatedInvoiceList,
    PaginationMeta,
)
from app.store import store

router = APIRouter(prefix="/v1/invoices", tags=["Invoices"])


@router.get("", response_model=PaginatedInvoiceList)
def list_invoices(
    cursor: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    status: InvoiceStatus | None = None,
) -> PaginatedInvoiceList:
    items = store.list_all()

    if status is not None:
        items = [item for item in items if item.status == status]

    start_index = 0
    if cursor is not None:
        ids = [str(item.id) for item in items]
        if cursor in ids:
            start_index = ids.index(cursor) + 1

    page = items[start_index : start_index + limit]
    has_more = start_index + limit < len(items)
    next_cursor = str(page[-1].id) if has_more and page else None

    return PaginatedInvoiceList(
        data=page,
        pagination=PaginationMeta(next_cursor=next_cursor, has_more=has_more, limit=limit),
    )


@router.post("", response_model=Invoice, status_code=201)
def create_invoice(payload: InvoiceCreateRequest) -> Invoice | Response:
    if store.invoice_number_exists(payload.invoice_number):
        return error_response(409, "INVOICE_CONFLICT", "Invoice number already exists.")

    return store.create(payload)


@router.get("/{invoice_id}", response_model=Invoice)
def get_invoice(invoice_id: UUID) -> Invoice | Response:
    invoice = store.get(invoice_id)
    if invoice is None:
        return error_response(404, "INVOICE_NOT_FOUND", "Invoice does not exist.")
    return invoice


@router.patch("/{invoice_id}", response_model=Invoice)
def update_invoice(invoice_id: UUID, payload: InvoiceUpdateRequest) -> Invoice | Response:
    try:
        invoice = store.update(invoice_id, payload)
    except ValueError:
        return error_response(409, "INVOICE_CONFLICT", "Invoice cannot be modified in its current state.")

    if invoice is None:
        return error_response(404, "INVOICE_NOT_FOUND", "Invoice does not exist.")
    return invoice


@router.delete("/{invoice_id}", status_code=204)
def void_invoice(invoice_id: UUID) -> Response:
    try:
        deleted = store.void(invoice_id)
    except ValueError:
        return error_response(409, "INVOICE_CONFLICT", "Invoice cannot be modified in its current state.")

    if not deleted:
        return error_response(404, "INVOICE_NOT_FOUND", "Invoice does not exist.")

    return Response(status_code=204)
