from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_subtract_two_numbers():
    response = client.post("/subtract", json={"a": 10, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": 3, "result": 7}


def test_subtract_negative_result():
    response = client.post("/subtract", json={"a": 2, "b": 5})

    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 5, "result": -3}


def test_subtract_invalid_type_returns_422():
    response = client.post("/subtract", json={"a": "abc", "b": 2})

    assert response.status_code == 422
