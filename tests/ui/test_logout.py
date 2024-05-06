from selene import browser, have

from qa_guru_diploma_altoro_api.utils.api_methods import successful_login, get_authorization_token


def test_logout(browser_management):

    auth_token = get_authorization_token()
    # headers = {'Authorization': auth_token}
    browser.open('/')

    script = f"document.cookie = 'Authorization={auth_token}';"
    browser.driver.execute_script(script)

    # Refresh the page to apply the cookie

    browser.driver.refresh()

    browser.element('#LoginLink').click()

    browser.element('#AccountLink .focus').should(have.text('ONLINE BANKING LOGIN'))


