import torch

from core.config import settings

REPOSITORY = "ultralytics/yolov5"
MODEL_TYPE = "custom"
MODEL_PATH = settings.base_dir / "ml" / "models" / "person" / "hands_above_head.pt"


model = torch.hub.load(REPOSITORY, MODEL_TYPE, path=MODEL_PATH)

model.conf = 0.4
model.iou = 0.45
model.agnostic = False
model.multi_label = False
model.classes = None
model.max_det = 1000
model.amp = False
