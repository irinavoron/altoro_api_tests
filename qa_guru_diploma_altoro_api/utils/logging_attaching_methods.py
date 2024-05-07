import json
from requests import Response
import allure
import logging

from allure_commons.types import AttachmentType


def allure_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name='request url',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    allure.attach(
        body=response.text,
        name='response text',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    allure.attach(
        body=str(response.status_code),
        name='response status code',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    allure.attach(
        body=str(response.cookies),
        name='response cookies',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(str(response.request.body)),
            name='request body',
            attachment_type=AttachmentType.JSON,
            extension='.json'
        )


def logging_info(response: Response):
    logging.info('Request url: ' + response.request.url)
    if response.request.body:
        logging.info('Request body: ' + str(response.request.body))
    logging.info('Response text: ' + response.text)
    logging.info('Response status code:' + str(response.status_code))
    logging.info('response headers: ' + str(response.headers))
