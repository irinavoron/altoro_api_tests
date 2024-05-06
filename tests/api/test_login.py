import json
import os

from dotenv import load_dotenv
import allure
import requests
from jsonschema import validate

from qa_guru_diploma_altoro_api.utils.api_methods import load_schema, api_request, get_authorization_token, \
    successful_login, unsuccessful_login

load_dotenv()
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')


def test_login_status_code_and_schema():
    schema = load_schema('successful_login_response.json')
    response = successful_login()
    response_body = response.json()

    assert response.status_code == 200
    with open(schema) as file:
        validate(response_body, json.loads(file.read()))


def test_successful_login_response_message():
    response = successful_login()
    response_body = response.json()

    assert response_body['success'] == f'{username} is now logged in'


def test_login_request_schema():
    schema = load_schema('login_request.json')
    request_data = {'username': username, 'password': password}

    with open(schema) as file:
        validate(request_data, json.loads(file.read()))


def test_user_is_logged_status_code_and_schema():
    schema = load_schema('loggedin_response.json')
    auth_token = get_authorization_token()
    headers = {'Authorization': auth_token}
    response = api_request(endpoint='/login', method='GET', headers=headers)
    response_body = response.json()

    assert response.status_code == 200
    with open(schema) as file:
        validate(response_body, json.loads(file.read()))


def test_user_is_logged_response_body():
    auth_token = get_authorization_token()
    headers = {'Authorization': auth_token}
    response = api_request(endpoint='/login', method='GET', headers=headers)
    response_body = response.json()

    assert response_body['loggedin'] == 'true'


def test_unsuccessful_login_status_code_and_schema():
    schema = load_schema('unsuccessful_login_response.json')
    response = unsuccessful_login()
    response_body = response.json()

    assert response.status_code == 400
    with open(schema) as file:
        validate(response_body, json.loads(file.read()))


def test_unsuccessful_login_response_body_error_message():
    response = unsuccessful_login()
    response_body = response.json()

    assert response_body['error'] == 'We\'re sorry, but this username or password was not found in our system.'

