import pytest
from selene import browser

from qa_guru_diploma_automationexercise_api.utils.api_methods import api_request

@pytest.fixture(scope='session')
def browser_management():
    browser.config.base_url = 'https://demo.testfire.net'


# @pytest.fixture
# def base_url():
#     base_url = 'https://automationexercise.com'
#
#     return base_url



