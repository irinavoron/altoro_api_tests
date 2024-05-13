import json
import allure
from allure_commons.types import Severity

from qa_guru_diploma_altoro_api.data import users
from qa_guru_diploma_altoro_api.utils import api_functions
from qa_guru_diploma_altoro_api.utils.allure_marks import layer, feature

pytestmark = [
    layer('api'),
    feature('admin options')
]

add_user_endpoint = '/api/admin/addUser'
change_password_endpoint = '/api/admin/changePassword'
method = 'POST'
success_message = 'Requested operation has completed successfully.'


@allure.title('Admin: Add new user: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_status_code_and_schema(admin_authorization_token):
    response = api_functions.add_new_user(admin_authorization_token, users.bilbo)

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_json_schema(response, 'admin_success_message_response.json')


@allure.title('Admin: Add new user: Success message verification')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_success_message(admin_authorization_token):
    response = api_functions.add_new_user(admin_authorization_token, users.bilbo)
    response_body = response.json()

    with allure.step('Verify the success message after adding a new user'):
        assert response_body['success'] == success_message


@allure.title('Admin: Add new user with incomplete data: Status code checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_add_new_user_incomplete_data_status_code(admin_authorization_token):
    headers = {'Authorization': admin_authorization_token}
    incomplete_payload = {
        "lastname": users.bilbo.lastname,
        "username": users.bilbo.username,
        "password1": users.bilbo.password1,
        "password2": users.bilbo.password2
    }
    json_payload = json.dumps(incomplete_payload)

    with allure.step('Try to add user by sending incomplete data'):
        response = api_functions.api_request(
            endpoint=add_user_endpoint,
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
        "firstname": users.bilbo.firstname,
        "lastname": users.bilbo.lastname,
        "username": users.bilbo.username,
        "password1": users.bilbo.password1,
        "password2": users.bilbo.password2
    }
    json_payload = json.dumps(payload)

    with allure.step('Try to add user without sending auth token'):
        response = api_functions.api_request(
            endpoint=add_user_endpoint,
            method=method,
            data=json_payload
        )

    api_functions.verify_status_code(response=response, expected_status_code=401)


@allure.title('Admin: Change user`s password: Status code and json schema checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_change_password_status_code_and_schema(admin_authorization_token):
    response = api_functions.change_password(admin_authorization_token, users.jdoe)

    api_functions.verify_status_code(response, 200)
    api_functions.verify_json_schema(response, 'admin_success_message_response.json')


@allure.title('Admin: Change user`s password: Success message verification')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_change_password_success_message(admin_authorization_token):
    response = api_functions.add_new_user(admin_authorization_token, users.jdoe)
    response_body = response.json()

    with allure.step('Verify the success message after changing user`s password'):
        assert response_body['success'] == success_message


@allure.title('Admin: Change user`s password without auth token: Status code checking')
@allure.tag('web')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_change_password_without_auth_token_status_code():
    payload = {
        "username": users.jdoe.username,
        "password1": users.jdoe.password1,
        "password2": users.jdoe.password2
    }
    json_payload = json.dumps(payload)

    with allure.step('Try to add user without sending auth token'):
        response = api_functions.api_request(
            endpoint=change_password_endpoint,
            method=method,
            data=json_payload
        )

    api_functions.verify_status_code(response=response, expected_status_code=401)
