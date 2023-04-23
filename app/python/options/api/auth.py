import os
import requests
import urllib.parse

from options.util.env import get_env_variable

TOKEN_URI = "https://api.tdameritrade.com/v1/oauth2/token"


def raise_if_error(response_data):
    if "error" in response_data:
        raise RuntimeError(f"Error getting token: {response_data}")


def generate_access_token() -> None:
    payload = {
        "grant_type": "authorization_code",
        "access_type": "offline",
        "code": urllib.parse.unquote(os.environ["AUTHORIZATION_CODE"]),
        "client_id": get_env_variable("TDAMERITRADE_CLIENT_ID"),
        "redirect_uri": get_env_variable("REDIRECT_URI"),
    }

    response = requests.post(TOKEN_URI, data=payload)
    response_data = response.json()

    raise_if_error(response_data)

    refresh_token = response_data["refresh_token"]

    print(f"Got refresh token: {refresh_token}")
    os.environ["TDAMERITRADE_REFRESH_TOKEN"] = refresh_token


def refresh_access_token() -> None:
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": get_env_variable("TDAMERITRADE_REFRESH_TOKEN"),
        "client_id": get_env_variable("TDAMERITRADE_CLIENT_ID"),
    }

    response = requests.post(TOKEN_URI, data=payload)
    response_data = response.json()

    raise_if_error(response_data)

    new_access_token = response_data["access_token"]
    return new_access_token
