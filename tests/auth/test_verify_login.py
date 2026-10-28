import requests
from configs.settings import BASE_URL
def test_verify_user_can_login_with_valid_credentials():
    payload={
    "email": "admin@example.com",
    "password": "AdminPassword123!"
    }
    response_body=requests.post(f"{BASE_URL}/api/v1/auth/login",json=payload)
    data=response_body.json()
    assert data["user"]["email"] == payload["email"]
    
def test_verify_user_can_login_with_invalid_credentials():
    payload={
        "email": "admin@example.com",
        "password": "AdminPassword123"
    } 
    response_body=requests.post(f"{BASE_URL}/api/v1/auth/login",json=payload)
    data=response_body.json()
    assert isinstance(data['error'],dict)
    assert data["error"]["code"] == 'INVALID_CREDENTIALs',f"Invalid Credentials it has to show {response_body.status_code}"