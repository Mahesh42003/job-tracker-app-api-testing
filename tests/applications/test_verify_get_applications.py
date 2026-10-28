import requests
from configs.settings import BASE_URL
def test_verify_authenticated_user_can_get_applications():
    #get jwt_token
    #login with user and get the token from response
    #make the api call with token in the header
    #verify the api status code
    #verify the api status body 
    payload={
    "email": "student@example1.com",
    "password": "12345678"
    }
    response_body=requests.post(f"{BASE_URL}/api/v1/auth/login",json=payload)
    data=response_body.json()
    bearer_token=data["access_token"]
    assert bearer_token
    assert response_body.status_code == 200
    headers={
        "Authorization":f"Bearer {bearer_token}"
    }
    response=requests.get(f"{BASE_URL}/api/v1/applications",headers=headers)
    assert isinstance(response.json(),list)
