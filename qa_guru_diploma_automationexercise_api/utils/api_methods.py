import os
from pathlib import Path
import allure
import requests
from dotenv import load_dotenv

base_url = 'https://demo.testfire.net/api'
load_dotenv()
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
invalid_user_name = os.getenv('INVALID_USER_NAME')


def load_schema(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))


def api_request(endpoint, method, data=None, params=None, **kwargs):
    url = base_url + endpoint
    with allure.step("API request"):
        response = requests.request(method, url, data=data, params=params, **kwargs)
        # response_attaching(response)
        return response


def successful_login():
    response = api_request(
        endpoint='/login',
        method='POST',
        json={'username': username, 'password': password}
    )

    return response


def get_authorization_token():
    response = successful_login()
    response_body = response.json()
    auth_token = response_body['Authorization']

    return auth_token


def unsuccessful_login():
    response = api_request(
        endpoint='/login',
        method='POST',
        json={'username': invalid_user_name, 'password': password}
    )

    return response
