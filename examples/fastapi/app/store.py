from __future__ import annotations

from copy import deepcopy
from uuid import UUID, uuid4

from app.schemas import Invoice, InvoiceCreateRequest, InvoiceLineItem, InvoiceStatus, InvoiceUpdateRequest, utc_now


class InvoiceStore:
    def __init__(self) -> None:
        self._items: dict[UUID, Invoice] = {}

    def seed(self, invoice: Invoice) -> None:
        self._items[invoice.id] = invoice

    def list_all(self) -> list[Invoice]:
        return sorted(self._items.values(), key=lambda item: item.created_at, reverse=True)

    def get(self, invoice_id: UUID) -> Invoice | None:
        return self._items.get(invoice_id)

    def invoice_number_exists(self, invoice_number: str) -> bool:
        return any(item.invoice_number == invoice_number for item in self._items.values())

    def create(self, payload: InvoiceCreateRequest) -> Invoice:
        now = utc_now()
        invoice = Invoice(
            id=uuid4(),
            customer_id=payload.customer_id,
            invoice_number=payload.invoice_number,
            status=InvoiceStatus.draft,
            currency=payload.currency,
            amount_due=sum(item.quantity * item.unit_amount for item in payload.line_items),
            due_date=payload.due_date,
            line_items=payload.line_items,
            created_at=now,
            updated_at=now,
        )
        self._items[invoice.id] = invoice
        return invoice

    def update(self, invoice_id: UUID, payload: InvoiceUpdateRequest) -> Invoice | None:
        current = self._items.get(invoice_id)
        if current is None:
            return None

        if current.status in {InvoiceStatus.paid, InvoiceStatus.void}:
            raise ValueError("conflict")

        updated = deepcopy(current)
        if payload.due_date is not None:
            updated.due_date = payload.due_date
        if payload.line_items is not None:
            updated.line_items = payload.line_items
            updated.amount_due = sum(item.quantity * item.unit_amount for item in payload.line_items)
        if payload.status is not None:
            if payload.status != InvoiceStatus.open or current.status != InvoiceStatus.draft:
                raise ValueError("conflict")
            updated.status = payload.status

        updated.updated_at = utc_now()
        self._items[invoice_id] = updated
        return updated

    def void(self, invoice_id: UUID) -> bool:
        current = self._items.get(invoice_id)
        if current is None:
            return False

        if current.status in {InvoiceStatus.paid, InvoiceStatus.void}:
            raise ValueError("conflict")

        current.status = InvoiceStatus.void
        current.updated_at = utc_now()
        self._items[invoice_id] = current
        return True


store = InvoiceStore()

sample_line_item = InvoiceLineItem(description="Platform subscription", quantity=1, unit_amount=1500.0)
store.seed(
    Invoice(
        id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        customer_id=UUID("7c9e6679-7425-40de-944b-e07fc1f90ae7"),
        invoice_number="INV-2026-0001",
        status=InvoiceStatus.draft,
        currency="THB",
        amount_due=1500.0,
        due_date=None,
        line_items=[sample_line_item],
        created_at=utc_now(),
        updated_at=utc_now(),
    )
)
