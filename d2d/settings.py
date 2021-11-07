import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    OPENAPI_URL = os.getenv('OPENAPI_URL')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

