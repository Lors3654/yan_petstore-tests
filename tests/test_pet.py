import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_pet():
    pet = {
        "id": 123,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Rex",
        "photoUrls": ["http://example.com/photo"],
        "tags": [{"id": 1, "name": "Cute"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_update_pet():
    pet = {
        "id": 123,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Max",
        "photoUrls": ["http://example.com/photo"],
        "tags": [{"id": 1, "name": "Cute"}],
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=pet)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"

def test_get_pet_by_id():
    pet_id = 123
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id

def test_delete_pet():
    pet_id = 123
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200

