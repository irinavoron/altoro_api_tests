import os

import pytest
from selene import browser
from dotenv import load_dotenv
from selene import browser, have
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

load_dotenv()
base_url = os.getenv('BASE_URL')
# username = os.getenv('USER_NAME')
# password = os.getenv('PASSWORD')
selenoid_url = os.getenv('SELENOID_URL')
selenoid_login = os.getenv('SELENOID_LOGIN')
selenoid_password = os.getenv('SELENOID_PASSWORD')


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    browser.quit()
