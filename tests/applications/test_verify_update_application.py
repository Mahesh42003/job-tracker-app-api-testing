from clients.api_client import APIClient
def test_verify_update_application():
    #Create a new application    
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
    api_client=APIClient() 
    post_endpoint="/api/v1/applications"
    response=api_client.post_data(post_endpoint,payload,expected_status_code=201)
    assert response.status_code == 201
    #update the application using patch
    payload={
        "status":"in_progress"
    } 
    application_id=response.json()["id"]
    patch_endpoint=f"/api/v1/applications/{application_id}"
    response=api_client.patch_data(patch_endpoint,body=payload,expected_status_code=200)
    assert response.json()["status"] == "in_progress"
