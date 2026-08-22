from unittest.mock import patch, MagicMock
from app import app
from Auth.jwt_handler import generate_token


def get_auth_header(role="user"):
    token = generate_token(user_id=1, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_add_to_cart_success():
    client = app.test_client()
    fake_cart = MagicMock()
    fake_cart.id = 1

    with patch("app.cart_repo.create_cart") as mock_cart, \
        patch("app.cart_repo.create_cart_item") as mock_item:
        mock_cart.return_value = fake_cart
        mock_item.return_value = MagicMock()

        response = client.post("/cart", json={"item_id": 1, "quantity": 2}, headers=get_auth_header())
        assert response.status_code == 201


def test_add_to_cart_item_not_found():
    client = app.test_client()
    fake_cart = MagicMock()
    fake_cart.id = 1

    with patch("app.cart_repo.create_cart") as mock_cart, \
        patch("app.cart_repo.create_cart_item") as mock_item:
        mock_cart.return_value = fake_cart
        mock_item.return_value = False

        response = client.post("/cart", json={"item_id": 999, "quantity": 2}, headers=get_auth_header())
        assert response.status_code == 404


def test_delete_cart_item_success():
    client = app.test_client()
    with patch("app.cart_repo.delete_cart_item") as mock:
        mock.return_value = True
        response = client.delete("/cart/1/1", headers=get_auth_header())
        assert response.status_code == 200