from selene import browser, have
import allure
from allure_commons.types import Severity
from qa_guru_diploma_altoro_api.utils.api_methods import set_auth_cookies


@allure.title('The language can be switched to English')
@allure.feature('Language')
@allure.tag('web')
@allure.story('The user can select English')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_switch_to_english():
    set_auth_cookies()

    with allure.step('Open Customize Site Language page'):
        browser.open('/bank/customize.jsp')
        browser.element('#MenuHyperLink5').click()
    with allure.step('Select English'):
        browser.element('#HyperLink2').click()

    with allure.step('Verify English is selected'):
        browser.element('[method="post"]').should(have.text('Current Language: english'))
