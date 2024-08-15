import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_user():
    user = {
        "id": 1,
        "username": "willsmith",
        "firstName": "Will",
        "lastName": "Smith",
        "email": "willsmith@example.com",
        "password": "12345",
        "phone": "1234567890",
        "userStatus": 0
    }
    response = requests.post(f"{BASE_URL}/user", json=user)
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert response_data["code"] == 200
    assert response_data["message"] == str(user["id"])

def test_get_user_by_username():
    username = "willsmith"
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
    assert response.json()["username"] == username

def test_update_user():
    username = "willsmith"
    user = {
        "id": 1,
        "username": username,
        "firstName": "Adam",
        "lastName": "Smith",
        "email": "adamsmith@example.com",
        "password": "54321",
        "phone": "0987654321",
        "userStatus": 0
    }
    response = requests.put(f"{BASE_URL}/user/{username}", json=user)
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert response_data["code"] == 200
    assert response_data["message"] == str(user["id"])

def test_delete_user():
    username = "willsmith"
    response = requests.delete(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
