from pydantic import BaseModel


class ConfidenceResponse(BaseModel):
    number: int
    confidence: list[float]
