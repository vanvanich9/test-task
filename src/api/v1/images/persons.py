from fastapi import APIRouter, Depends, UploadFile

from common.api.exceptions import HTTPBadRequest, HTTPNotFound
from schemas.responses.images import ConfidenceResponse
from services.image.person import PersonImageService, get_person_image_service

router = APIRouter()


@router.post(
    "/hands-above-head",
    summary="Detect person with hands above head",
    description="Receive image and detect only one person with hands above head",
    response_description="Confidence that person with hands above head",
)
async def hands_above_head(
    file: UploadFile = Depends(PersonImageService.validate_file_image),
    image_service: PersonImageService = Depends(get_person_image_service),
):
    confidence = await image_service.confidence_hands_above_head(file)

    if len(confidence) == 0:
        raise HTTPNotFound("Hands above head not found.")
    if len(confidence) > 1:
        raise HTTPBadRequest("Too many hands above head(-s).")

    return ConfidenceResponse(confidence=confidence[0])
