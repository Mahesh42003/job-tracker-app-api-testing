from clients.api_client import APIClient
def test_verify_authenticated_user_can_get_applications():
    #get jwt_token
    #login with user and get the token from response
    #make the api call with token in the header
    #verify the api status code
    #verify the api status body 
    api_client=APIClient()
    response=api_client.get(f"/api/v1/applications",headers=None)
    
    assert isinstance(response.json(),list)

