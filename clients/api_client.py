import requests
class APIClient:
    def __init__(self):
        pass
    def get_data(self,url):
        self.url=url
        response_body=requests.get(url)
        assert response_body.status_code == 200    
        return response_body.json()