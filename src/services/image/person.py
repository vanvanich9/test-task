from functools import lru_cache
from typing import IO

from services.image.base import ImageService


class PersonImageService(ImageService):
    def __init__(self):
        pass

    async def similarity_hands_above_head(self, image: IO) -> float:
        # TODO: Implement function in the next tasks
        return 0.5


@lru_cache()
def get_person_image_service():
    return PersonImageService()
