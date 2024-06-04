from pydantic import BaseModel


class ConfidenceResponse(BaseModel):
    confidence: float
