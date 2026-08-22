from unittest.mock import patch
from app import app


def test_register_success():
    client = app.test_client()

    with patch("app.user_repo.register") as mock_register:
        mock_register.return_value = True

        response = client.post("/register", json={
            "name": "Juan",
            "username": "juanp",
            "email": "juan@gmail.com",
            "password": "1234"
        })

        assert response.status_code == 201
        assert response.json["message"] == "User created"


def test_register_missing_field():
    client = app.test_client()

    response = client.post("/register", json={
        "name": "Juan",
        "username": "juanp",
        "email": "juan@gmail.com"
        # falta password
    })

    assert response.status_code == 400
    assert "password" in response.json["message"]


def test_register_email_already_exists():
    client = app.test_client()

    with patch("app.user_repo.register") as mock_register:
        mock_register.return_value = False  

        response = client.post("/register", json={
            "name": "Juan",
            "username": "juanp",
            "email": "juan@gmail.com",
            "password": "1234"
        })

        assert response.status_code == 409


def test_register_username_already_exists():
    client = app.test_client()

    with patch("app.user_repo.register") as mock_register:
        mock_register.return_value = None  

        response = client.post("/register", json={
            "name": "Juan",
            "username": "juanp",
            "email": "juan@gmail.com",
            "password": "1234"
        })

        assert response.status_code == 409


def test_login_success():
    client = app.test_client()

    with patch("app.user_repo.login") as mock_login:
        mock_login.return_value = "fake.jwt.token"

        response = client.post("/login", json={
            "email": "juan@gmail.com",
            "password": "1234"
        })

        assert response.status_code == 200
        assert "token" in response.json


def test_login_invalid_credentials():
    client = app.test_client()

    with patch("app.user_repo.login") as mock_login:
        mock_login.return_value = False

        response = client.post("/login", json={
            "email": "juan@gmail.com",
            "password": "wrongpassword"
        })

        assert response.status_code == 401