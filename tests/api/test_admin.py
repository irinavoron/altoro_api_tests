import json

from qa_guru_diploma_altoro_api.utils import api_functions


def test_add_new_user_status_code_and_schema(admin_authorization_token):
    headers = {'Authorization': admin_authorization_token}
    payload = {
        "firstname": "Bilbo",
        "lastname": "Baggins",
        "username": "bilbob",
        "password1": "S3l3ctS0methingStr0ng5AsP@ssword",
        "password2": "S3l3ctS0methingStr0ng5AsP@ssword"
    }

    json_payload = json.dumps(payload)

    response = api_functions.api_request(
        endpoint='/api/admin/addUser',
        method='POST',
        data=json_payload,
        headers=headers
    )

    api_functions.verify_status_code(response=response, expected_status_code=200)
    api_functions.verify_json_schema(response, 'admin_add_user_response.json')
