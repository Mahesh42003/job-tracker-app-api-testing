
def create_application(api_client, payload=None, expected_status_code=201):

    if payload is None:
        payload = build_application_payload()

    response = api_client.post_data(
        "/api/v1/applications",
        payload,
        expected_status_code=expected_status_code
    )

    return response
def get_application(api_client,application_id):
    response=api_client.get_data(f"/api/v1/applications/{application_id}")
    return response
def build_application_payload():
    """
    Builds the payload for creating a new application.
    """
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
    return payload