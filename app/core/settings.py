from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    APP_NAME: str
