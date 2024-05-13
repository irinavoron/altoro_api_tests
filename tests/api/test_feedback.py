from qa_guru_diploma_altoro_api.utils import api_functions


def test_feedback_valid_data_status_code_and_schema(authorization_token):
    # headers = {'Authorization': authorization_token}
    payload = {
        'name': "J Smith",
        'email': "jsmtih@altoromutual.com",
        'subject': "Amazing web design",
        'message': "I like the new look of your application"
    }

    response = api_functions.api_request(
        endpoint='/api/feedback/submit',
        method='POST',
        json=payload
        # headers=headers
    )

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_json_schema(response=response, schema_title='feedback_response.json')


def test_feedback_invalid_data_status_code():
    payload = {
        'email': "jsmtih@altoromutual.com",
        'subject': "Amazing web design",
        'message': "I like the new look of your application"
    }

    response = api_functions.api_request(
        endpoint='/api/feedback/submit',
        method='POST',
        json=payload
    )

    api_functions.verify_status_code(response=response, expected_status_code=400)
