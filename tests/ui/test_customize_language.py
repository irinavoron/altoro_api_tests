from selene import browser, have

from qa_guru_diploma_altoro_api.utils.api_methods import set_auth_cookies


def test_switch_to_english():
    set_auth_cookies()
    browser.open('https://demo.testfire.net/bank/customize.jsp')
    browser.element('#HyperLink2').click()
    browser.element('[method="post"]').should(have.text('Current Language: english'))
