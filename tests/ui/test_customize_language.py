from selene import browser, have
import allure
from allure_commons.types import Severity

from qa_guru_diploma_altoro_api.utils.allure_marks import layer, feature
from qa_guru_diploma_altoro_api.utils import api_functions

pytestmark = [
    layer('ui'),
    feature('language')
]


@allure.title('The language can be switched to English')
@allure.tag('web')
@allure.story('The user can select English')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_switch_to_english():
    api_functions.set_auth_cookies_for_ui_tests()

    with allure.step('Open Customize Site Language page'):
        browser.open('/bank/customize.jsp')
        browser.element('#MenuHyperLink5').click()
    with allure.step('Select English'):
        browser.element('#HyperLink2').click()

    with allure.step('Verify English is selected'):
        browser.element('[method="post"]').should(have.text('Current Language: english'))
