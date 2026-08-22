from unittest.mock import patch, MagicMock
from app import app
from Auth.jwt_handler import generate_token


def get_auth_header(role="user"):
    token = generate_token(user_id=1, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_create_invoice_success():
    client = app.test_client()
    fake_invoice = MagicMock()
    fake_invoice.id = 1

    with patch("app.invoice_repo.create_invoice") as mock:
        mock.return_value = fake_invoice
        response = client.post("/invoice", json={
            "address_id": 1, "pay_method_id": 1
        }, headers=get_auth_header())
        assert response.status_code == 201


def test_create_invoice_empty_cart():
    client = app.test_client()
    with patch("app.invoice_repo.create_invoice") as mock:
        mock.return_value = None
        response = client.post("/invoice", json={
            "address_id": 1, "pay_method_id": 1
        }, headers=get_auth_header())
        assert response.status_code == 404


def test_create_invoice_not_enough_stock():
    client = app.test_client()
    with patch("app.invoice_repo.create_invoice") as mock:
        mock.return_value = "Not enough stock for Shampoo"
        response = client.post("/invoice", json={
            "address_id": 1, "pay_method_id": 1
        }, headers=get_auth_header())
        assert response.status_code == 400