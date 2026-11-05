from helpers.application_helper import build_application_payload,create_application
from clients.api_client import APIClient 


def test_verify_create_application_required_company_name():
    payload = build_application_payload()
    api_client=APIClient()
    payload.pop("company_name")
    response=create_application(api_client,payload,expected_status_code=422)
    result=response.json()
    assert result["error"],f"Create a application with missing field response like {result[error]}"
    assert result["error"]["code"] == "VALIDATION_ERROR"
    assert result["error"]["details"][0]["loc"][1] == "company_name"
def test_verifyapplications__list_requires_authentication():
    api_client=APIClient(authenticated=False)
    get_applications_endpoint=f"/api/v1/applications"
    get_response=api_client.get_data(get_applications_endpoint,expected_status_code=401)
    assert get_response['error']['code'] == "AUTHENTICATION_REQUIRED"
    assert get_response['error']['details'] == []
    assert get_response['error']['message'] == 'Authentication required'