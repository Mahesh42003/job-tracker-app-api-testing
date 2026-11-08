
import pytest
from clients.api_client import APIClient


@pytest.mark.tcid("001")
def test_verify_public_demo_stats():
    """Verify demo stats response contains expected fields and types."""

    url = "/api/v1/public/demo-stats"

    api_client = APIClient()
    response = api_client.get_data(url)

    assert isinstance(response, dict)
    assert len(response.keys()) == 2

    assert isinstance(response["total_seeded_applications"], int)
    assert isinstance(response["status_counts"], dict)

    status_counts = response["status_counts"]

    for key, value in status_counts.items():
        print(f"{key}: {value}")
        assert isinstance(value, int)
