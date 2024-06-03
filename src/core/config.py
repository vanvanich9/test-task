import os
from logging import config as logging_config
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    project_name: str = Field(default='service', validation_alias='PROJECT_NAME')
    debug: bool = Field(default=False, validation_alias='DEBUG')

    base_dir: Path = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


settings = Settings()
