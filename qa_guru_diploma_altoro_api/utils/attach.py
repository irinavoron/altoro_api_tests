import os

import allure
from selene import browser
from allure_commons.types import AttachmentType


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs():
    logs = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(body=logs, name='logs', attachment_type=AttachmentType.TEXT, extension='.log')


def add_html():
    html = browser.driver.page_source
    allure.attach(body=html, name='html', attachment_type=AttachmentType.HTML, extension='.html')


def add_video():
    selenoid_url = os.getenv('SELENOID_URL')
    video_url = f'https://{selenoid_url}/video/{browser.driver.session_id}.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(body=html, name='video', attachment_type=AttachmentType.HTML, extension='.html')
