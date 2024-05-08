import os
from pathlib import Path
import allure
import requests
from dotenv import load_dotenv
from allure_commons.types import AttachmentType

from qa_guru_diploma_altoro_api.utils.logging_attaching_methods import response_and_request_attaching, response_and_request_logging

load_dotenv()
base_url = os.getenv('BASE_URL')
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
invalid_user_name = os.getenv('INVALID_USER_NAME')


def load_schema(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))


def api_request(endpoint, method, data=None, params=None, **kwargs):
    url = base_url + endpoint
    response = requests.request(method, url, data=data, params=params, **kwargs)

    response_and_request_attaching(response)
    response_and_request_logging(response)

    return response


def successful_login():
    with allure.step('Login via API'):
        response = api_request(
            endpoint='/login',
            method='POST',
            json={'username': username, 'password': password}
        )

        return response


def get_authorization_token():
    response = successful_login()
    response_body = response.json()
    with allure.step('Get authorization token from response body'):
        auth_token = response_body['Authorization']

        allure.attach(
            body=auth_token,
            name='authorization token',
            attachment_type=AttachmentType.TEXT,
            extension='.txt'
        )

    return auth_token


def unsuccessful_login():
    with allure.step('Try to login with invalid credentials'):
        response = api_request(
            endpoint='/login',
            method='POST',
            json={'username': invalid_user_name, 'password': password}
        )

        return response
