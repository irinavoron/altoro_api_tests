import json

import allure
from allure_commons.types import Severity

from qa_guru_diploma_altoro_api.data import users
from qa_guru_diploma_altoro_api.utils import api_functions
from qa_guru_diploma_altoro_api.utils.allure_marks import layer, feature

endpoint = '/api/admin/addUser'
method = 'POST'

pytestmark = [
    layer('api'),
    feature('admin options')
]


@allure.title('Admin: Add new user: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_status_code_and_schema(admin_authorization_token):
    response = api_functions.add_new_user(admin_authorization_token, users.Bilbo)

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_json_schema(response, 'admin_add_user_response.json')


@allure.title('Admin: Add new user: Success message verification')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_success_message(admin_authorization_token):
    response = api_functions.add_new_user(admin_authorization_token, users.Bilbo)
    response_body = response.json()

    with allure.step('Verify the success message after adding a new user'):
        assert response_body['success'] == 'Requested operation has completed successfully.'


@allure.title('Admin: Add new user with incomplete data: Status code checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_incomplete_data_status_code(admin_authorization_token):
    headers = {'Authorization': admin_authorization_token}
    incomplete_payload = {
        "lastname": users.Bilbo.lastname,
        "username": users.Bilbo.username,
        "password1": users.Bilbo.password1,
        "password2": users.Bilbo.password2
    }
    json_payload = json.dumps(incomplete_payload)

    with allure.step('Try to add user by sending incomplete data'):
        response = api_functions.api_request(
            endpoint=endpoint,
            method=method,
            data=json_payload,
            headers=headers
        )
    api_functions.verify_status_code(response=response, expected_status_code=400)


@allure.title('Admin: Add new user without auth token: Status code checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_without_auth_token_status_code():
    payload = {
        "firstname": users.Bilbo.firstname,
        "lastname": users.Bilbo.lastname,
        "username": users.Bilbo.username,
        "password1": users.Bilbo.password1,
        "password2": users.Bilbo.password2
    }
    json_payload = json.dumps(payload)

    with allure.step('Try to add user without sending auth token'):
        response = api_functions.api_request(
            endpoint=endpoint,
            method=method,
            data=json_payload
        )

    api_functions.verify_status_code(response=response, expected_status_code=401)




