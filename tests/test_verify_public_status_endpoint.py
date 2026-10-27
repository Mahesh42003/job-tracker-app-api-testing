import requests
def test_verify_public_status_endpoint():
    url='http://localhost:3050/api/v1/public/status'
    response=requests.get(url)
    status_code=response.status_code
    assert status_code == 200 ,f"The status should return 200"
    response_body=response.json()
    assert response_body["api_version"] == 'v1'
    assert response_body["app_name"] == 'SuperSQA Job Tracker'
    assert response_body["environment"] == 'local'
