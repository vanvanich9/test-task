from fastapi import APIRouter, Depends, UploadFile


from schemas.responses.images import ConfidenceResponse
from services.image.person import PersonImageService, get_person_image_service

router = APIRouter()


@router.post(
    "/hands-above-head",
    summary="Detect persons with hands above head",
    description="Receive image and detect all persons with hands above head",
    response_description="Number of persons with hands above head and confidences",
)
async def hands_above_head(
    file: UploadFile = Depends(PersonImageService.validate_file_image),
    image_service: PersonImageService = Depends(get_person_image_service),
):
    confidence = await image_service.confidence_hands_above_head(file)
    return ConfidenceResponse(number=len(confidence), confidence=confidence)
