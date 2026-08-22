from unittest.mock import patch, MagicMock
from app import app
from Auth.jwt_handler import generate_token


def get_auth_header(role="admin"):
    token = generate_token(user_id=1, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_create_return_success():
    client = app.test_client()
    with patch("app.return_repo.create_return") as mock:
        mock.return_value = MagicMock()
        response = client.post("/return", json={
            "invoice_item_id": 1, "quantity": 2
        }, headers=get_auth_header())
        assert response.status_code == 201


def test_create_return_exceeds_amount():
    client = app.test_client()
    with patch("app.return_repo.create_return") as mock:
        mock.return_value = "Return quantity exceeds available amount"
        response = client.post("/return", json={
            "invoice_item_id": 1, "quantity": 100
        }, headers=get_auth_header())
        assert response.status_code == 400