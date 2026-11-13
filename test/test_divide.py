from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_divide_two_numbers():
    response = client.post("/divide", json={"a": 10, "b": 2})

    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": 2, "result": 5.0}


def test_divide_decimal_numbers():
    response = client.post("/divide", json={"a": 7, "b": 2})

    assert response.status_code == 200
    assert response.json() == {"a": 7, "b": 2, "result": 3.5}


def test_divide_by_zero_returns_400():
    response = client.post("/divide", json={"a": 10, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}
