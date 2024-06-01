from pydantic import BaseModel, Field


class SimilarityResponse(BaseModel):
    similarity: float = Field(ge=0, le=1)
