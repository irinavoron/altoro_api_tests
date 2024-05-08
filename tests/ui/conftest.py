import os

import pytest
from selene import browser
from dotenv import load_dotenv
from selene import browser, have
import requests

import pytest


load_dotenv()
base_url = os.getenv('BASE_URL')
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    load_dotenv()
    browser.config.base_url = os.getenv('BASE_URL')









