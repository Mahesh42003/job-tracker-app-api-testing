import requests
from configs.settings import BASE_URL
from clients.api_client import APIClient
def test_verify_public_demo_stats():
    
    url=f"{BASE_URL}/api/v1/public/demo-stats"
    api_client=APIClient()
    response=api_client.get_data(url)
    assert len(response.keys()) == 2
    assert isinstance(response["total_seeded_applications"],int)
    assert isinstance(response["status_counts"],dict) 
    status_counts=response["status_counts"]
    breakpoint()

    for k,v in status_counts.items():
        print(f"{k},{v}")
        assert isinstance(v,int)