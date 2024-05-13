import json
from pathlib import Path
import allure
import requests
from requests import Response
from allure_commons.types import AttachmentType
from selene import browser
from jsonschema import validate

from config import config
from qa_guru_diploma_altoro_api.data.users import User
from qa_guru_diploma_altoro_api.utils.logging_attaching_methods import response_and_request_attaching, \
    response_and_request_logging


def load_schema(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))


# def load_schema(schema_name):
#     return str(Path(__file__).parent.parent / 'schemas' / schema_name)


def api_request(endpoint, method, data=None, params=None, **kwargs):
    url = config.BASE_URL + endpoint
    response = requests.request(method, url, data=data, params=params, **kwargs)

    response_and_request_attaching(response)
    response_and_request_logging(response)

    return response


def successful_login(user_name, password):
    with allure.step('Login via API'):
        response = api_request(
            endpoint='/api/login',
            method='POST',
            json={'username': user_name, 'password': password}
        )

        return response


# def get_authorization_token():
#     response = successful_login()
#     response_body = response.json()
#     with allure.step('Get authorization token from response body'):
#         auth_token = response_body['Authorization']
#
#         allure.attach(
#             body=auth_token,
#             name='authorization token',
#             attachment_type=AttachmentType.TEXT,
#             extension='.txt'
#         )
#
#     return auth_token


def unsuccessful_login(invalid_user_name):
    with allure.step('Try to login with invalid credentials'):
        response = api_request(
            endpoint='/api/login',
            method='POST',
            json={'username': invalid_user_name, 'password': config.PASSWORD}
        )

        return response


def set_auth_cookies_for_ui_tests():
    url = config.BASE_URL + "/doLogin"
    payload = {'uid': config.USER_NAME, 'passw': config.PASSWORD, 'btnSubmit': 'Login'}

    with allure.step('Get authorization cookies'):
        with requests.Session() as session:
            session.post(url, data=payload)

            cookie = session.cookies

    with allure.step('Open main page'):
        browser.open(config.BASE_URL)

    with allure.step('Set authorization cookies'):
        for cookie_name in ["JSESSIONID", "AltoroAccounts"]:
            browser.driver.add_cookie({"name": cookie_name, "value": cookie.get(cookie_name)})


def verify_status_code(response: Response, expected_status_code):
    with allure.step('Verify the status code'):
        assert response.status_code == expected_status_code


def verify_json_schema(response: Response, schema_title):
    schema = load_schema(schema_title)

    with allure.step('Validate the response json schema'):
        with open(schema) as file:
            validate(response.json(), json.loads(file.read()))


def add_new_user(auth_token, user: User):
    headers = {'Authorization': auth_token}
    payload = {
        "firstname": user.firstname,
        "lastname": user.lastname,
        "username": user.username,
        "password1": user.password1,
        "password2": user.password2
    }
    json_payload = json.dumps(payload)
    with allure.step('Add new user'):
        response = api_request(
            endpoint='/api/admin/addUser',
            method='POST',
            data=json_payload,
            headers=headers
        )
    return response
