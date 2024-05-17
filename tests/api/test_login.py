import allure
from allure_commons.types import Severity

from config import config
from altoro_api_tests.utils import api_functions
from altoro_api_tests.utils.allure_marks import layer, feature

pytestmark = [
    layer('api'),
    feature('login')
]


@allure.title('Successful login: Check status code, json schema and response body')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_login_response_body():
    response = api_functions.successful_login(config.USER_NAME, config.PASSWORD)

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_response_json_schema(
        response=response,
        schema_title='successful_login_response.json'
    )
    api_functions.verify_message_in_response_body(
        response=response,
        key='success',
        response_message=f'{config.USER_NAME} is now logged in'
    )


@allure.title('Checking the login request json schema')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_login_request_schema():
    api_functions.verify_request_json_schema(
        schema_title='login_request.json',
        payload={'username': config.USER_NAME, 'password': config.PASSWORD}
    )


@allure.title('Unsuccessful login: Check status code, json schema and response body')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_login_response_body():
    response = api_functions.unsuccessful_login('no name')

    api_functions.verify_status_code(
        response=response,
        expected_status_code=400
    )
    api_functions.verify_response_json_schema(
        response=response,
        schema_title='unsuccessful_login_response.json'
    )
    api_functions.verify_message_in_response_body(
        response=response,
        key='error',
        response_message='We\'re sorry, but this username or password was not found in our system.'
    )
