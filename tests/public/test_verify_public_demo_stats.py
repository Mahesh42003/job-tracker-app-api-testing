import requests
from configs.settings import BASE_URL
def test_verify_public_demo_stats():
    
    url=f"{BASE_URL}/api/v1/public/demo-stats"
    response=requests.get(url)
    status_code=response.status_code 
    assert status_code == 200
    #checking data-type is correct or not 
    response_body=response.json()
    assert len(response_body.keys()) == 2
    assert isinstance(response_body["total_seeded_applications"],int)
    assert isinstance(response_body["status_counts"],dict) 
    status_counts=response_body["status_counts"]

    for k,v in status_counts.items():
        print(f"{k},{v}")
        assert isinstance(v,int)