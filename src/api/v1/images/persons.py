from fastapi import APIRouter, Depends, File, UploadFile

from schemas.responses.images import SimilarityResponse
from services.image.person import PersonImageService, get_person_image_service

router = APIRouter()


@router.post(
    "/hands-above-head",
    summary="",
    description="",
    response_description="",
)
async def hands_above_head(
    image: UploadFile = File(...),
    image_service: PersonImageService = Depends(get_person_image_service),
):
    await image_service.filter_file_image(image)
    similarity = await image_service.similarity_hands_above_head(image)
    return SimilarityResponse(similarity=similarity)
