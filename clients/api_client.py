import logging
import requests
from configs.settings import BASE_URL, DEFAULT_EMAIL, DEFAULT_PASSWORD
logger=logging.getLogger(__name__)

class APIClient:
    """Client for making authenticated and unauthenticated API requests."""

    def __init__(
        self,
        authenticated=True,
        email=DEFAULT_EMAIL,
        password=DEFAULT_PASSWORD
    ):
        """Initialize the client and optionally authenticate.

        Args:
            authenticated: Whether to log in and add a bearer token to
                subsequent requests.
            email: Email address used when authenticating.
            password: Password used when authenticating.

        Raises:
            AssertionError: If the login request returns an unexpected status
                code.
            requests.RequestException: If the login request fails.
        """
        self.authenticated = authenticated
        self.headers = {}

        if authenticated:
            logger.info("successfully authenticated")
            access_token = self.login(email, password)
            self.headers["Authorization"] = f"Bearer {access_token}"

    def login(self, email, password):
        """Authenticate and return the access token.

        Args:
            email: Account email address.
            password: Account password.

        Returns:
            The access token returned by the API.

        Raises:
            AssertionError: If the login request returns an unexpected status
                code.
            requests.RequestException: If the login request fails.
            KeyError: If the response does not contain an ``access_token``.
        """

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
        """Send a GET request and return the response.

        Args:
            endpoint: API path to request.
            headers: Optional headers to add to or override client headers.
            expected_status_code: HTTP status code expected from the response.

        Returns:
            The ``requests.Response`` object.

        Raises:
            AssertionError: If the response status code differs from the
                expected code.
            requests.RequestException: If the request fails.
        """

        url = self.build_url(endpoint)

        response = requests.get(
            url,
            headers=self.build_headers(headers)
        )

        self.verify_status_code(response, expected_status_code, url)

        return response

    def get_data(self, endpoint, headers=None, expected_status_code=200):
        """Send a GET request and return the decoded JSON response.

        Args:
            endpoint: API path to request.
            headers: Optional headers to add to or override client headers.
            expected_status_code: HTTP status code expected from the response.

        Returns:
            The response body decoded from JSON.

        Raises:
            AssertionError: If the response status code differs from the
                expected code.
            requests.RequestException: If the request fails.
            requests.exceptions.JSONDecodeError: If the response body is not
                valid JSON.
        """

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
        """Send a POST request with a JSON payload.

        Args:
            endpoint: API path to request.
            payload: Data to serialize as the request's JSON body.
            headers: Optional headers to add to or override client headers.
            expected_status_code: HTTP status code expected from the response.

        Returns:
            The ``requests.Response`` object.

        Raises:
            AssertionError: If the response status code differs from the
                expected code.
            requests.RequestException: If the request fails.
        """

        url = self.build_url(endpoint)

        response = requests.post(
            url,
            json=payload,
            headers=self.build_headers(headers)
        )

        self.verify_status_code(response, expected_status_code, url)

        return response

    def build_headers(self, headers=None):
        """Combine client headers with optional request-specific headers.

        Request-specific values override client values with the same key.

        Args:
            headers: Optional headers to merge into the client headers.

        Returns:
            A new dictionary containing the merged headers.
        """

        return {**self.headers, **(headers or {})}

    def verify_status_code(self, response, expected_status_code, url):
        """Assert that a response has the expected HTTP status code.

        Args:
            response: Response object to check.
            expected_status_code: HTTP status code expected from the response.
            url: Request URL, included in the assertion message.

        Raises:
            AssertionError: If the response status code does not match the
                expected code.
        """

        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"but got {response.status_code} for {url}. "
            f"Response: {response.text}"
        )

    def build_url(self, endpoint):
        """Join the configured base URL with an API endpoint.

        Args:
            endpoint: API path to append to the base URL.

        Returns:
            The complete URL with duplicate boundary slashes removed.
        """

        return f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"
