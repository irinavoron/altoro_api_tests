import os
from pathlib import Path
import allure
import requests
from dotenv import load_dotenv
from allure_commons.types import AttachmentType
from selene import browser, have

from qa_guru_diploma_altoro_api.utils.logging_attaching_methods import response_and_request_attaching, \
    response_and_request_logging

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
            endpoint='/api/login',
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
            endpoint='/api/login',
            method='POST',
            json={'username': invalid_user_name, 'password': password}
        )

        return response


# def get_auth_cookies():
#     url = base_url + "/doLogin"
#     payload = {'uid': username, 'passw': password, 'btnSubmit': 'Login'}
#
#     with requests.Session() as session:
#         session.post(url, data=payload)
#
#         cookie = session.cookies
#         return cookie
#
#
# def set_auth_cookies():
#     login_cookies = get_auth_cookies()
#     browser.open(base_url)
#
#     for cookie_name in ["JSESSIONID", "AltoroAccounts"]:
#         browser.driver.add_cookie({"name": cookie_name, "value": login_cookies.get(cookie_name)})


# def test_customize_language():
#     set_auth_cookies()
#     browser.open('https://demo.testfire.net/bank/customize.jsp')
#     browser.element('#HyperLink2').click()
#     browser.element('[method="post"]').should(have.text('Current Language: english'))

def set_auth_cookies():
    url = base_url + "/doLogin"
    payload = {'uid': username, 'passw': password, 'btnSubmit': 'Login'}

    with requests.Session() as session:
        session.post(url, data=payload)

        cookie = session.cookies

    browser.open(base_url)

    for cookie_name in ["JSESSIONID", "AltoroAccounts"]:
        browser.driver.add_cookie({"name": cookie_name, "value": cookie.get(cookie_name)})


