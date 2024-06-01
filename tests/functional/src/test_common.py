import pytest

from tests.functional.testdata.common import PING_RESPONSE
from tests.functional.utils.schemas import Response


@pytest.mark.asyncio()
async def test_ping(make_request):
    response: Response = await make_request('/api/ping')

    assert response.status == PING_RESPONSE.status
    assert response.body == PING_RESPONSE.body
