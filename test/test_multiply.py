from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_multiply_two_numbers():
    response = client.post("/multiply", json={"a": 4, "b": 5})

    assert response.status_code == 200
    assert response.json() == {"a": 4, "b": 5, "result": 20}


def test_multiply_decimal_numbers():
    response = client.post("/multiply", json={"a": 2.5, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"a": 2.5, "b": 4, "result": 10.0}


def test_multiply_invalid_type_returns_422():
    response = client.post("/multiply", json={"a": "abc", "b": 2})

    assert response.status_code == 422
