import allure
from allure_commons.types import Severity

from altoro_api_tests.utils import api_functions
from altoro_api_tests.utils.allure_marks import layer, feature

pytestmark = [
    layer('api'),
    feature('feedback')
]


@allure.title('Feedback: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.MINOR)
def test_feedback_valid_data_status_code_and_schema():
    payload = {
        'name': "J Smith",
        'email': "jsmtih@altoromutual.com",
        'subject': "Amazing web design",
        'message': "I like the new look of your application"
    }

    with allure.step('Submit feedback'):
        response = api_functions.api_request(
            endpoint='/api/feedback/submit',
            method='POST',
            json=payload
        )

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_response_json_schema(response=response, schema_title='feedback_response.json')


@allure.title('Feedback with incomplete data: Status code checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.MINOR)
def test_feedback_with_incomplete_data_status_code():
    payload = {
        'email': "jsmtih@altoromutual.com",
        'subject': "Amazing web design",
        'message': "I like the new look of your application"
    }

    with allure.step('Submit feedback with incomplete data'):
        response = api_functions.api_request(
            endpoint='/api/feedback/submit',
            method='POST',
            json=payload
        )

    api_functions.verify_status_code(response=response, expected_status_code=400)
