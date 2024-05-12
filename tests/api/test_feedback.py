from qa_guru_diploma_altoro_api.utils import api_functions


def test_feedback_status_code_and_schema():
    auth_token = api_functions.get_authorization_token()
    headers = {'Authorization': auth_token}
    payload = {
        'name': "J Smith",
        'email': "jsmtih@altoromutual.com",
        'subject': "Amazing web design",
        'message': "I like the new look of your application"
    }

    response = api_functions.api_request(
        endpoint='/api/feedback/submit',
        method='POST',
        json=payload,
        headers=headers
    )

    api_functions.verify_status_code_and_schema(response, 200, 'feedback_response.json')
