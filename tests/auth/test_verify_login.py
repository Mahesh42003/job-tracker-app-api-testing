import requests
from clients.api_client import APIClient
api_client=APIClient()
def test_verify_user_can_login_with_valid_credentials():
    payload={
    "email": "admin@example.com",
    "password": "AdminPassword123!"
    }
    response_body=api_client.post_data(f"/api/v1/auth/login",payload=payload)
    data=response_body.json()
    assert data["user"]["email"] == payload["email"]
    
def test_verify_user_can_login_with_invalid_credentials():
    payload={
        "email": "admin@example.com",
        "password": "AdminPassword123"
    } 
    response_body=api_client.post_data(f"/api/v1/auth/login",payload=payload,expected_status_code=401)
    data=response_body.json()
    assert isinstance(data['error'],dict)
    assert data["error"]["code"] == 'INVALID_CREDENTIALS',f"Invalid Credentials it has to show {response_body.status_code}"