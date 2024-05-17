from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from config import config
from altoro_api_tests.utils import attach


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.base_url = config.BASE_URL

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
        command_executor=f"https://{config.SELENOID_LOGIN}:{config.SELENOID_PASSWORD}@{config.SELENOID_URL}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot()
    attach.add_html()
    attach.add_logs()
    attach.add_video()

    browser.quit()
