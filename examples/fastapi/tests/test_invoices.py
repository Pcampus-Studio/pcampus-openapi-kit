from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_invoices() -> None:
    response = client.get("/v1/invoices")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert "pagination" in body
    assert len(body["data"]) >= 1


def test_get_invoice_not_found() -> None:
    response = client.get("/v1/invoices/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "INVOICE_NOT_FOUND"


def test_create_invoice_conflict() -> None:
    payload = {
        "customer_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
        "invoice_number": "INV-2026-0001",
        "currency": "THB",
        "line_items": [{"description": "Duplicate", "quantity": 1, "unit_amount": 100}],
    }
    response = client.post("/v1/invoices", json=payload)
    assert response.status_code == 409
    assert response.json()["error"]["code"] == "INVOICE_CONFLICT"


def test_create_and_void_invoice() -> None:
    payload = {
        "customer_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
        "invoice_number": "INV-2026-TEST-001",
        "currency": "THB",
        "line_items": [{"description": "Consulting", "quantity": 2, "unit_amount": 500}],
    }
    create_response = client.post("/v1/invoices", json=payload)
    assert create_response.status_code == 201
    invoice_id = create_response.json()["id"]

    void_response = client.delete(f"/v1/invoices/{invoice_id}")
    assert void_response.status_code == 204

    get_response = client.get(f"/v1/invoices/{invoice_id}")
    assert get_response.status_code == 200
    assert get_response.json()["status"] == "void"
