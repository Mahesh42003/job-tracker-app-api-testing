from clients.api_client import APIClient
def test_verify_create_application():
    #create a payload for creating an application
    payload={
        "company_name": "Wells Fargo",
        "job_url": "https://wells.com/jobs/ui-test-engineer",
        "location": "London, UK",
        "next_action": "Follow up with hr",
        "notes": "Submitted through company linkedin app.",
        "remote_type": "hybrid",
        "role_title": "UI Test Engineer",
        "salary_range": "$100,000 - $120,000",
        "status": "potential"
    }

    #create an api using api_client
    api_client=APIClient()
    endpoint="/api/v1/applications"
    #make a post request to create an application
    response=api_client.post_data(endpoint,payload=payload,expected_status_code=201)
    assert response.json()["company_name"] == payload["company_name"],f"Expected company name {payload['company_name']} but got {response.json()['company_name']}"
    assert response.json()["job_url"] == payload["job_url"],f"Expected job url {payload['job_url']} but got {response.json()['job_url']}"
    assert response.json()["location"] == payload["location"],f"Expected location {payload['location']} but got {response.json()['location']}"
    assert response.json()["next_action"] == payload["next_action"],f"Expected next action {payload['next_action']} but got {response.json()['next_action']}"
    assert response.json()["notes"] == payload["notes"],f"Expected notes {payload['notes']} but got {response.json()['notes']}"
    assert response.json()["remote_type"] == payload["remote_type"],f"Expected remote type {payload['remote_type']} but got {response.json()['remote_type']}"
    assert response.json()["role_title"] == payload["role_title"],f"Expected role title {payload['role_title']} but got {response.json()['role_title']}"
    assert response.json()["salary_range"] == payload["salary_range"],f"Expected salary range {payload['salary_range']} but got {response.json()['salary_range']}"
    assert response.json()["status"] == payload["status"],f"Expected status {payload['status']} but got {response.json()['status']}"
    assert "id" in response.json(),f"Expected id in response but got {response.json()}"
    assert "created_at" in response.json(),f"Expected created_at in response but got {response.json()}"
    assert "updated_at" in response.json(),f"Expected updated_at in response but got {response.json()}" 
    #Getting data from the response after creating the application using GET request to verify the application is created successfully
    application_id=response.json()["id"]
    application_id_endpoint=f"/api/v1/applications/{application_id}"
    get_response=api_client.get_data(application_id_endpoint,expected_status_code=200)
    assert get_response["company_name"] == payload["company_name"],f"Expected company name {payload['company_name']} but got {get_response.json()['company_name']}"
    assert get_response["job_url"] == payload["job_url"],f"Expected job url {payload['job_url']} but got {get_response.json()['job_url']}"
    assert get_response["location"] == payload["location"],f"Expected location {payload['location']} but got {get_response.json()['location']}"
    assert get_response["next_action"] == payload["next_action"],f"Expected next action {payload['next_action']} but got {get_response.json()['next_action']}"
    assert get_response["notes"] == payload["notes"],f"Expected notes {payload['notes']} but got {get_response.json()['notes']}"
    assert get_response["remote_type"] == payload["remote_type"],f"Expected remote type {payload['remote_type']} but got {get_response.json()['remote_type']}"
    assert get_response["role_title"] == payload["role_title"],f"Expected role title {payload['role_title']} but got {get_response.json()['role_title']}"
    assert get_response["salary_range"] == payload["salary_range"],f"Expected salary range {payload['salary_range']} but got {get_response.json()['salary_range']}"
    assert get_response["status"] == payload["status"],f"Expected status {payload['status']} but got {get_response.json()['status']}"

    #clear / tear down the created application after the test is completed
    delete_application_endpoint=f"/api/v1/applications/{application_id}"
    delete_response=api_client.delete(delete_application_endpoint,expected_status_code=204)
    assert delete_response.status_code == 204,f"Expected status code 204 but got {delete_response.status_code}"