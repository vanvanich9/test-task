from typing import Any

import cv2
import numpy as np
from fastapi import File, UploadFile
from pandas import DataFrame

from common.api.exceptions import HTTPBadRequest

ACCEPTED_FILE_TYPES = [
    "image/png",
    "image/jpeg",
    "image/jpg",
    "image/heic",
    "image/heif",
    "image/heics",
    "png",
    "jpeg",
    "jpg",
    "heic",
    "heif",
    "heics",
]


class ImageService:
    @staticmethod
    async def validate_file_image(file: UploadFile = File(...)) -> UploadFile:
        if file.content_type not in ACCEPTED_FILE_TYPES:
            raise HTTPBadRequest()

        return file

    def run_model(self, model: Any, contents: bytes) -> DataFrame:
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        result = model(img, size=640)
        data_frame = result.pandas().xyxy[0]
        return data_frame
