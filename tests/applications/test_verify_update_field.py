from clients.api_client import APIClient
from helpers.application_helper import create_application,get_application
def test_verify_create_valid_application():
    """Verify that a valid application can be created successfully."""
    # Implementation for testing the creation of a valid application  
    api_client=APIClient()  
    response = create_application(api_client)
    assert response.status_code == 201
    #update the application
    application_id=response.json()["id"]
    data={
        "notes":"API automated testing"
    }
    updated_response=api_client.patch_data(f"/api/v1/applications/{application_id}",data,expected_status_code=200)
    #get the application
    get_response=get_application(api_client,application_id)
    breakpoint()
