import requests
class APIClient:
    def __init__(self):
        pass
    def get_data(self,url,headers):
        self.url=url
        response_body=requests.get(url)
        assert response_body.status_code == 200 
        return response_body.json()
    def post_data(url,payload,expected_status_code=200):
        response_body=requests.post(url,json=payload) 
        assert response_body.status_code == expected_status_code
        return response_body