import os

import pytest
from selene import browser
from dotenv import load_dotenv


@pytest.fixture(scope='session')
def browser_management():
    load_dotenv()
    browser.config.base_url = os.getenv('BASE_URL')




