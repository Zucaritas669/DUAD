from unittest.mock import patch, MagicMock
from app import app
from Auth.jwt_handler import generate_token


def get_auth_header(role="admin"):
    token = generate_token(user_id=1, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_create_category_success():
    client = app.test_client()
    with patch("app.category_repo.create_category") as mock:
        mock.return_value = True
        response = client.post("/category", json={"name": "Perros"}, headers=get_auth_header())
        assert response.status_code == 201


def test_create_category_missing_name():
    client = app.test_client()
    response = client.post("/category", json={}, headers=get_auth_header())
    assert response.status_code == 400


def test_create_category_already_exists():
    client = app.test_client()
    with patch("app.category_repo.create_category") as mock:
        mock.return_value = False
        response = client.post("/category", json={"name": "Perros"}, headers=get_auth_header())
        assert response.status_code == 409


def test_edit_category_success():
    client = app.test_client()
    with patch("app.category_repo.edit_category") as mock:
        mock.return_value = True
        response = client.patch("/category/1", json={"name": "Gatos"}, headers=get_auth_header())
        assert response.status_code == 200


def test_edit_category_not_found():
    client = app.test_client()
    with patch("app.category_repo.edit_category") as mock:
        mock.return_value = False
        response = client.patch("/category/1", json={"name": "Gatos"}, headers=get_auth_header())
        assert response.status_code == 404


def test_edit_category_name_exists():
    client = app.test_client()
    with patch("app.category_repo.edit_category") as mock:
        mock.return_value = None
        response = client.patch("/category/1", json={"name": "Gatos"}, headers=get_auth_header())
        assert response.status_code == 409


def test_delete_category_success():
    client = app.test_client()
    with patch("app.category_repo.delete_category") as mock:
        mock.return_value = True
        response = client.delete("/category/1", headers=get_auth_header())
        assert response.status_code == 200


def test_delete_category_not_found():
    client = app.test_client()
    with patch("app.category_repo.delete_category") as mock:
        mock.return_value = False
        response = client.delete("/category/1", headers=get_auth_header())
        assert response.status_code == 404


def test_get_all_categories_success():
    client = app.test_client()
    with patch("app.category_repo.get_all") as mock:
        fake_category = MagicMock()
        fake_category.id = 1
        fake_category.name = "Perros"
        fake_category.description = None

        mock.return_value = [fake_category]

        response = client.get("/category", headers=get_auth_header())
        assert response.status_code == 200

