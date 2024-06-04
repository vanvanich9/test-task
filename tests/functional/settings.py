import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

SAMPLE_ACCESS_TOKEN_EXPIRE = 60 * 60
SAMPLE_REFRESH_TOKEN_EXPIRE = 30 * 24 * 60 * 60


class TestSettings(BaseSettings):
    app_schema: str = Field(default='http', validation_alias='APP_SCHEMA')
    app_host: str = Field(default='127.0.0.1', validation_alias='APP_HOST')
    app_port: int = Field(default=8000, validation_alias='APP_PORT')

    base_dir: Path = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    @property
    def app_url(self):
        return f'{self.app_schema}://{self.app_host}:{self.app_port}'


test_settings = TestSettings()
