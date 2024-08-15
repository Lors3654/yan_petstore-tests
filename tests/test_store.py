import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

def test_get_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_create_order():
    order = {
        "id": 1,
        "petId": 123,
        "quantity": 1,
        "shipDate": "2024-08-14T21:31:12.646Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/store/order", json=order)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

def test_get_order_by_id():
    order_id = 1
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_delete_order():
    order_id = 1
    response = requests.delete(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200