import pytest
import allure
from allure_commons.types import AttachmentType

from config import config
from altoro_api_tests.utils import api_functions


@pytest.fixture
def admin_authorization_token():
    response = api_functions.successful_login(config.ADMIN_USER_NAME, config.ADMIN_PASSWORD)
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
