from enum import Enum

import torch

from core.config import settings


class PersonClassesEnum(int, Enum):
    HANDS_ABOVE_HEAD = 0


person_model = torch.hub.load(
    repo_or_dir=settings.person_repository,
    model=settings.person_model,
    path=settings.person_custom_model_path,
    source=settings.person_source,
)
person_model.conf = 0.4
person_model.iou = 0.45
person_model.agnostic = False
person_model.multi_label = False
person_model.classes = None
person_model.max_det = 1000
person_model.amp = False
