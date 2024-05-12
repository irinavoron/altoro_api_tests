import pytest
import allure
from allure_commons.types import AttachmentType

from qa_guru_diploma_altoro_api.utils import api_functions


@pytest.fixture
def authorization_token():
    response = api_functions.successful_login()
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
