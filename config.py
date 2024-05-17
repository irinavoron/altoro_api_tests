from dotenv import load_dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str

    SELENOID_URL: str
    SELENOID_LOGIN: str
    SELENOID_PASSWORD: str

    USER_NAME: str
    PASSWORD: str

    ADMIN_USER_NAME: str
    ADMIN_PASSWORD: str


load_dotenv()
config = Config()
