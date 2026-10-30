import requests
from configs.settings import BASE_URL,DEFAULT_EMAIL,DEFAULT_PASSWORD

def login_user(email=DEFAULT_EMAIL,password=DEFAULT_PASSWORD):
    """Log in a user and return the API access token.

    Args:
        email: Account email address. Defaults to the configured email.
        password: Account password. Defaults to the configured password.

    Returns:
        The access token from the login response.

    Raises:
        requests.RequestException: If the login request fails.
        requests.exceptions.JSONDecodeError: If the response body is not valid
            JSON.
        KeyError: If the response does not contain an ``access_token``.
    """
    payload={
    "email": email,
    "password": password
    }
    response_body=requests.post(f"{BASE_URL}/api/v1/auth/login",json=payload)
    data=response_body.json()
    return data["access_token"] 
