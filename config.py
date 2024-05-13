from dotenv import load_dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://demo.testfire.net'

    SELENOID_URL: str = 'selenoid.autotests.cloud'
    SELENOID_LOGIN: str
    SELENOID_PASSWORD: str

    USER_NAME: str
    PASSWORD: str

    ADMIN_USER_NAME: str
    ADMIN_PASSWORD: str


load_dotenv()
config = Config()
