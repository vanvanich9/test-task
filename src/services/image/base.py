from typing import IO

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
    async def filter_file_image(self, file: IO):
        if file.content_type not in ACCEPTED_FILE_TYPES:
            raise HTTPBadRequest()
