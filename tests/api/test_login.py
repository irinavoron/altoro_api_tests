import json
import os
from dotenv import load_dotenv
import allure
from allure_commons.types import Severity
from jsonschema import validate

from qa_guru_diploma_altoro_api.utils import api_functions
from qa_guru_diploma_altoro_api.utils.allure_marks import layer, feature

load_dotenv()
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

pytestmark = [
    layer('api'),
    feature('login')
]


@allure.title('Successful login: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_login_status_code_and_schema():
    schema = api_functions.load_schema('successful_login_response.json')
    response = api_functions.successful_login()
    response_body = response.json()

    with allure.step('Verify the status code'):
        assert response.status_code == 200
    with allure.step('Validate the response json schema'):
        with open(schema) as file:
            validate(response_body, json.loads(file.read()))


@allure.title('Successful login: Checking the message in the response body')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_successful_login_response_message():
    response = api_functions.successful_login()
    response_body = response.json()

    with allure.step('Check the message in the response body'):
        assert response_body['success'] == f'{username} is now logged in'


@allure.title('Checking the login request json schema')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_login_request_schema():
    schema = api_functions.load_schema('login_request.json')
    request_data = {'username': username, 'password': password}

    with allure.step('Validate the request json schema'):
        with open(schema) as file:
            validate(request_data, json.loads(file.read()))


@allure.title('Unsuccessful login: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_login_status_code_and_schema():
    schema = api_functions.load_schema('unsuccessful_login_response.json')
    response = api_functions.unsuccessful_login('no name')
    response_body = response.json()

    with allure.step('Verify the status code'):
        assert response.status_code == 400
    with allure.step('Validate the response json schema'):
        with open(schema) as file:
            validate(response_body, json.loads(file.read()))


@allure.title('Unsuccessful login: Checking the message in the response body')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_unsuccessful_login_response_body_error_message():
    response = api_functions.unsuccessful_login('no name')
    response_body = response.json()

    with allure.step('Check the error message in the response body'):
        assert response_body['error'] == 'We\'re sorry, but this username or password was not found in our system.'
