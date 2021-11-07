import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    OPENAPI_URL = os.getenv('OPENAPI_URL')

