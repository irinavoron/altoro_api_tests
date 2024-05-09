import os
from dotenv import load_dotenv


load_dotenv()
base_url = os.getenv('BASE_URL')

selenoid_url = os.getenv('SELENOID_URL')
selenoid_login = os.getenv('SELENOID_LOGIN')
selenoid_password = os.getenv('SELENOID_PASSWORD')

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
