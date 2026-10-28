import requests
from configs.settings import BASE_URL
from helpers.auth_helper import login_user
def test_verify_authenticated_user_can_get_applications():
    #get jwt_token
    #login with user and get the token from response
    #make the api call with token in the header
    #verify the api status code
    #verify the api status body 
    bearer_token=login_user()
    assert bearer_token
    headers={
        "Authorization":f"Bearer {bearer_token}"
    }
    response=requests.get(f"{BASE_URL}/api/v1/applications",headers=headers)
    breakpoint()
    assert isinstance(response.json(),list)
