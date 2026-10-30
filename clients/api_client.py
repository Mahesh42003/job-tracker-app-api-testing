
import requests
from configs.settings import BASE_URL, DEFAULT_EMAIL, DEFAULT_PASSWORD


class APIClient:

    def __init__(
        self,
        authenticated=True,
        email=DEFAULT_EMAIL,
        password=DEFAULT_PASSWORD
    ):
        self.authenticated = authenticated
        self.headers = {}

        if authenticated:
            access_token = self.login(email, password)
            self.headers["Authorization"] = f"Bearer {access_token}"

    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response_body = self.post_data(
            endpoint="/api/v1/auth/login",
            payload=payload
        )

        data = response_body.json()
        return data["access_token"]

    def get(self, endpoint, headers=None, expected_status_code=200):

        url = self.build_url(endpoint)

        response = requests.get(
            url,
            headers=self.build_headers(headers)
        )

        self.verify_status_code(response, expected_status_code, url)

        return response

    def get_data(self, endpoint, headers=None, expected_status_code=200):

        url = self.build_url(endpoint)

        response_body = requests.get(
            url,
            headers=self.build_headers(headers)
        )

        self.verify_status_code(response_body, expected_status_code, url)

        return response_body.json()

    def post_data(
        self,
        endpoint,
        payload,
        headers=None,
        expected_status_code=200
    ):

        url = self.build_url(endpoint)

        response = requests.post(
            url,
            json=payload,
            headers=self.build_headers(headers)
        )

        self.verify_status_code(response, expected_status_code, url)

        return response

    def build_headers(self, headers=None):

        return {**self.headers, **(headers or {})}

    def verify_status_code(self, response, expected_status_code, url):

        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"but got {response.status_code} for {url}. "
            f"Response: {response.text}"
        )

    def build_url(self, endpoint):

        return f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"
