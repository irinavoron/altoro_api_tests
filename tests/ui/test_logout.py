from selene import browser, have

from qa_guru_diploma_altoro_api.utils.api_methods import api_request, get_authorization_token


def go_to_customize_language(endpoint, **kwargs):
    response = api_request(
        endpoint=endpoint,
        method='GET',
        **kwargs
    )

    return response


def test_customize_language(browser_management):
    auth_token = get_authorization_token()
    headers = {'Authorization': auth_token}

    browser.open('/')
    go_to_customize_language(endpoint='/bank/customize.jsp', headers=headers)

    browser.element('#HyperLink2').click()

    browser.element('[method="post"]').should(have.text('english'))
