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

    person_repository: str = Field(default='yolov5', validation_alias='PERSON_REPOSITORY')
    person_model: str = Field(default='custom', validation_alias='PERSON_MODEL')
    person_custom_model: str = Field(default='person.pt', validation_alias='PERSON_CUSTOM_MODEL')
    person_source: str = Field(default='local', validation_alias='PERSON_SOURCE')

    base_dir: Path = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    @property
    def person_custom_model_path(self) -> Path:
        return self.base_dir / 'ml' / 'image' / 'models' / self.person_custom_model

    @property
    def person_repository_path(self) -> Path:
        return self.base_dir / self.person_repository


settings = Settings()
