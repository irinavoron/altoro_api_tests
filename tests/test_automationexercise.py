import json

import allure
import requests
from jsonschema import validate

from qa_guru_diploma_automationexercise_api.utils.api_methods import load_schema

base_url = 'https://demo.testfire.net/api'


def api_request(endpoint, method, data=None, params=None, **kwargs):
    url = base_url + endpoint
    with allure.step("API request"):
        response = requests.request(method, url, data=data, params=params, **kwargs)
        # response_attaching(response)
        return response


def test_login():
    schema = load_schema('login.json')
    response = api_request(endpoint='/login', method='POST', json={"username": "jsmith", "password": "demo1234"})
    response_body = response.json()

    assert response.status_code == 200
    with open(schema) as file:
        validate(response_body, json.loads(file.read()))
