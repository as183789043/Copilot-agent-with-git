from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_add_two_numbers():
    response = client.post("/add", json={"a": 10, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": 3, "result": 13}


def test_add_negative_numbers():
    response = client.post("/add", json={"a": -2, "b": 5})

    assert response.status_code == 200
    assert response.json() == {"a": -2, "b": 5, "result": 3}


def test_add_invalid_type_returns_422():
    response = client.post("/add", json={"a": "abc", "b": 2})

    assert response.status_code == 422
