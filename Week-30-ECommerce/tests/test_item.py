from unittest.mock import patch
from app import app
from Auth.jwt_handler import generate_token


def get_auth_header(role="admin"):
    token = generate_token(user_id=1, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_create_item_success():
    client = app.test_client()
    with patch("app.item_repo.create_item") as mock:
        mock.return_value = True
        response = client.post("/item", json={
            "name": "Shampoo", "category_id": 1, "stock": 10, "price": 5.99
        }, headers=get_auth_header())
        assert response.status_code == 201


def test_create_item_missing_field():
    client = app.test_client()
    response = client.post("/item", json={"name": "Shampoo"}, headers=get_auth_header())
    assert response.status_code == 400


def test_create_item_name_exists():
    client = app.test_client()
    with patch("app.item_repo.create_item") as mock:
        mock.return_value = False
        response = client.post("/item", json={
            "name": "Shampoo", "category_id": 1, "stock": 10, "price": 5.99
        }, headers=get_auth_header())
        assert response.status_code == 409


def test_create_item_category_not_found():
    client = app.test_client()
    with patch("app.item_repo.create_item") as mock:
        mock.return_value = None
        response = client.post("/item", json={
            "name": "Shampoo", "category_id": 1, "stock": 10, "price": 5.99
        }, headers=get_auth_header())
        assert response.status_code == 404


def test_edit_item_success():
    client = app.test_client()
    with patch("app.item_repo.edit_item") as mock:
        mock.return_value = True
        response = client.patch("/item/1", json={
            "name": "Shampoo", "category_id": 1, "stock": 10, "price": 5.99
        }, headers=get_auth_header())
        assert response.status_code == 200


def test_delete_item_success():
    client = app.test_client()
    with patch("app.item_repo.delete_item") as mock:
        mock.return_value = True
        response = client.delete("/item/1", headers=get_auth_header())
        assert response.status_code == 200


def test_get_all_items_success():
    client = app.test_client()
    with patch("app.item_repo.get_all_items") as mock:
        mock.return_value = [{"id": 1, "name": "Shampoo"}]
        response = client.get("/item", headers=get_auth_header())
        assert response.status_code == 200