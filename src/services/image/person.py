from functools import lru_cache

from fastapi import UploadFile

from ml.image.person import PersonClassesEnum, person_model
from services.image.base import ImageService


class PersonImageService(ImageService):
    async def confidence_hands_above_head(self, file: UploadFile) -> list[float]:
        contents = await file.read()
        data_frame = self.run_model(model=person_model, contents=contents)
        return data_frame[
            data_frame['class'] == PersonClassesEnum.HANDS_ABOVE_HEAD
        ]['confidence'].to_list()


@lru_cache()
def get_person_image_service() -> PersonImageService:
    return PersonImageService()
