from pathlib import Path
import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser

import config
from qa_guru_diploma_altoro_api.utils.logging_attaching_methods import response_and_request_attaching, \
    response_and_request_logging


def load_schema(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))


def api_request(endpoint, method, data=None, params=None, **kwargs):
    url = config.base_url + endpoint
    response = requests.request(method, url, data=data, params=params, **kwargs)

    response_and_request_attaching(response)
    response_and_request_logging(response)

    return response


def successful_login():
    with allure.step('Login via API'):
        response = api_request(
            endpoint='/api/login',
            method='POST',
            json={'username': config.username, 'password': config.password}
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


def unsuccessful_login(invalid_user_name):
    with allure.step('Try to login with invalid credentials'):
        response = api_request(
            endpoint='/api/login',
            method='POST',
            json={'username': invalid_user_name, 'password': config.password}
        )

        return response


def set_auth_cookies():
    url = config.base_url + "/doLogin"
    payload = {'uid': config.username, 'passw': config.password, 'btnSubmit': 'Login'}

    with allure.step('Get authorization cookies'):
        with requests.Session() as session:
            session.post(url, data=payload)

            cookie = session.cookies

    with allure.step('Open main page'):
        browser.open(config.base_url)

    with allure.step('Set authorization cookies'):
        for cookie_name in ["JSESSIONID", "AltoroAccounts"]:
            browser.driver.add_cookie({"name": cookie_name, "value": cookie.get(cookie_name)})
