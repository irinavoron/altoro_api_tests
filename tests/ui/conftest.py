import os
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from qa_guru_diploma_altoro_api.utils import attach

load_dotenv()
base_url = os.getenv('BASE_URL')

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

    attach.add_screenshot()
    attach.add_html()
    attach.add_logs()
    attach.add_video()

    browser.quit()
