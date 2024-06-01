from fastapi import APIRouter

from schemas.responses.common import PingPongResponse

router = APIRouter()


@router.get(
    '/',
    summary='Ping API',
    description='Ping API for check health',
    response_description='Pong, if service alive',
)
async def ping() -> PingPongResponse:
    return PingPongResponse()
